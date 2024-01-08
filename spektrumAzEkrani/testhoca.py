from termios import FF1
import numpy as np
import adi
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def calculate_spec(samples, db_scale = True):
    spec = np.abs(np.fft.fftshift(np.fft.fft(samples)))
    if db_scale:
        return np.log10(spec)
    else:
        return spec

c = 3e8
f1_norm = (1e3)/50e6
f2_norm = (2.5e7)/50e6
dfdt = (2.5e7-1e3)/(10000000*20e-9)
# dfdt = (f2_norm-f1_norm)/

def plot_norm_spec(samples, fig_num = 1, title = None):
    x_axis = np.linspace(-0.5, 0.5, len(samples))
    plt.figure(fig_num)
    plt.plot(x_axis, samples)
    if title is not None:
        plt.title(title)
    peaks = find_peaks(samples)[0]
    print( peaks)
    peaks_values = samples[peaks]
    # ind= np.argpartition(samples,-4)[-4:]
    # y_top = samples[ind]
    ind= np.argpartition(peaks_values,-4)[-4:]
    y_top = peaks_values[ind]
    ind  = peaks[ind]
    # ind = peaks
    # print(ind)
    for i,j in zip(x_axis[ind],y_top):
        print("%s and %s" % (i, j))
        plt.text(i, j, '({}, {})'.format(i, j))
    ind = np.sort(ind)
    plt.text(0, 5, 'diff %s' % (x_axis[ind[1]] - x_axis[ind[0]] ))
    plt.text(0, 5.2, 'diff %s' % (x_axis[ind[2]] - x_axis[ind[3]] ))
    diff = (x_axis[ind[1]] - x_axis[ind[0]] )
    diff = diff*50e6
    diff_dist = (c * abs(diff))/(2*dfdt)
    print('%s * %s / 2 * %s' % (c, diff, dfdt))
    print('dist: %s' % diff_dist)
    plt.show()


sample_rate = 50e6 # MHz
center_freq = 2.40e9 # Hz 2.45GHz
num_samps = 10000000 # number of samples per call to rx()
singal_real = True

sdr = adi.Pluto("ip:192.168.2.1")
sdr.sample_rate = int(sample_rate)

# Config Tx
sdr.tx_rf_bandwidth = int(sample_rate) # filter cutoff, just set it to the same as sample rate
sdr.tx_lo = int(center_freq)
sdr.tx_hardwaregain_chan0 = -10 # Increase to increase tx power, valid range is -90 to 0 dB

# Config Rx
sdr.rx_lo = int(center_freq)
sdr.rx_rf_bandwidth = int(sample_rate)
sdr.rx_buffer_size = num_samps
sdr.gain_control_mode_chan0 = 'manual'
sdr.rx_hardwaregain_chan0 = 0.0 # dB, increase to increase the receive gain, but be careful not to saturate the ADC


N = int(num_samps)
print("N: %s" % N)
t = np.arange(N)/sample_rate
f = np.linspace(start=1e3, stop=(2.5e7), num=N)
print(f)
# f = np.arange(start=1e3, stop=(25e2+ 1e3), step=25)
print(len(t))
print(len(f))
if singal_real:
    tx_samples = 0.5*np.sin(2.0*np.pi*np.multiply(f,t)) # Simulate real chirp 
else:
    tx_samples = 0.5*np.exp(2.0j*np.pi*np.multiply(f,t)) # Simulate complex chirp 


# tx_samples = np.concatenate((tx_samples, np.zeros(N)))
print(np.min(np.real(tx_samples)), np.max(np.real(tx_samples)))
print(np.min(np.imag(tx_samples)), np.max(np.imag(tx_samples)))

spec_tx = calculate_spec(tx_samples)
f = np.linspace(sample_rate/-2, sample_rate/2, len(spec_tx))
# Plot freq domain
plt.figure(1)
plt.plot(f/2e6, spec_tx)
plt.xlabel("Frequency [MHz]")
plt.ylabel("PSD")

fmcw_samples = []
for i in range(0,1):
    fmcw_samples = np.concatenate((fmcw_samples, tx_samples))

tx_samples *= 2**14 # The PlutoSDR expects samples to be between -2^14 and +2^14, not -1 and +1 like some SDRs
# Start the transmitter
sdr.tx_cyclic_buffer = True # Enable cyclic buffers
sdr.tx(tx_samples) # start transmitting


# Clear buffer just to be safe
for i in range (0, 5):
    raw_data = sdr.rx()


# Receive samples
total_samples = []
total_samples = np.asarray(total_samples)
for i in range(0,1):
    rx_samples = sdr.rx()
    total_samples = np.concatenate((total_samples, rx_samples))

# Stop transmitting
sdr.tx_destroy_buffer()


fmcw_samples = np.multiply(fmcw_samples, np.max(total_samples))

plt.figure(2)
fmcw_result_samples = np.multiply(total_samples, fmcw_samples)
plot_norm_spec(calculate_spec(fmcw_result_samples), 2, "FMCW Result")

plt.figure(3)
plt.title("Recived signal spec")
plt.plot(f/2e6, calculate_spec(total_samples))

plt.figure(4)
plt.plot(f/2e6, calculate_spec(total_samples))
fig, axs = plt.subplots(2,1)
axs[0].plot(total_samples)
axs[1].plot(fmcw_result_samples)

plt.figure(5)
NFFT = 1024
fig, axs =  plt.subplots(2,1)
axs[0].plot(total_samples)
axs[1].plot(fmcw_samples)
# axs[0].specgram(fmcw_samples, NFFT=NFFT, Fs=sample_rate, noverlap=900)
# axs[1].specgram(total_samples, NFFT=NFFT, Fs=sample_rate, noverlap=900)
plt.show()
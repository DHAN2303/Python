import adi
import time
import matplotlib.pyplot as plt
import numpy as np

sdr = adi.Pluto(uri='ip:192.168.2.1')
sample_rate = 50e6 # MHz
center_freq = 2.40e9 # Hz 2.45GHz
num_samps = 10000000 # number of samples per call to rx()

sdr.rx_lo = int(center_freq)
sdr.rx_rf_bandwidth = int(sample_rate)
sdr.rx_buffer_size = num_samps
sdr.gain_control_mode_chan0 = 'manual'
sdr.rx_hardwaregain_chan0 = 0.0 # dB, increase to inc

plt.plot(np.abs(sdr.rx()))
plt.xlabel("frequency [MHz]")
plt.ylabel("dBfs")
plt.draw()
plt.show()
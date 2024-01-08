import numpy as np
import adi
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk

sample_rate = 50e6 # MHz
center_freq = 2.40e9 # Hz 2.45GHz
num_samps = 1000000 # number of samples per call to rx()
fft_size = 1024 # size of FFT window
sdr = adi.Pluto(uri="ip:192.168.2.1")

sdr.rx_lo = int(center_freq)
sdr.rx_rf_bandwidth = int(sample_rate)
sdr.rx_buffer_size = num_samps
sdr.gain_control_mode_chan0 = 'manual'
sdr.rx_hardwaregain_chan0 = 0.0 # dB, increase to inc

root = tk.Tk()
root.title("ADALM-PLUTO Real-time Signal and Spectrum Waterfall")

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(5, 5))
line1, = ax1.plot(np.abs(sdr.rx()))
spec_data = np.zeros((1000, fft_size//2))
spec = ax2.imshow(spec_data, origin="lower", aspect="auto", cmap="jet", vmin=-120, vmax=0)
cbar_ax = fig.add_axes([0.85, 0.2, 0.05, 0.6])  # Add axis for colorbar
cbar = fig.colorbar(spec, cax=cbar_ax)

ax1.set_ylabel("Amplitude (V)")
ax2.set_xlabel("Time (samples)")
ax2.set_ylabel("Frequency (Hz)")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

toolbar_frame = tk.Frame(master=root)
toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
toolbar.update()
toolbar.pack(side=tk.BOTTOM, fill=tk.X)
toolbar_frame.pack(side=tk.BOTTOM, fill=tk.X)

def update_signal():
    signal = np.abs(sdr.rx())
    line1.set_ydata(signal)
    # Compute FFT on a sliding window of samples
    for i in range(spec_data.shape[0]-1):
        spec_data[i] = spec_data[i+1]
    window = signal[-fft_size:]
    spec_data[-1] = 10 * np.log10(np.abs(np.fft.fft(window))[:fft_size//2])
    spec.set_data(spec_data)
    canvas.draw()
    root.after(50, update_signal)

update_signal()
root.mainloop()

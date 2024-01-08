import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

root = tk.Tk()
root.title("Real-time Sine Wave and Waterfall Spectrum")

fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 1000)
line, = ax.plot(x, np.sin(x))
ax.set_ylim(-1, 1)
ax.set_xlim(0, 2*np.pi)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Amplitude")

spectrum_ax = plt.axes([0.125, 0.75, 0.775, 0.2], facecolor='k')
spectrum, = spectrum_ax.plot([], [], lw=2, color='cyan')
spectrum_ax.set_xlim(0, 50)
spectrum_ax.set_ylim(-80, 10)
spectrum_ax.set_xlabel("Frequency (Hz)")
spectrum_ax.set_ylabel("Magnitude (dB)")

def update(frame):
    line.set_ydata(np.sin(x + frame/10.0))
    spectrum.set_data(np.fft.rfftfreq(len(x), 1/1000),
                      20 * np.log10(np.abs(np.fft.rfft(np.sin(x + frame/10.0)))))

ani = animation.FuncAnimation(fig, update, frames=100, interval=100)

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.mainloop()

import numpy as np
import adi
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
import tkinter.messagebox

pluto = adi.Pluto(uri="ip:192.168.2.1")

root = tk.Tk()
root.title("ADALM-PLUTO Real-time Signal and Spectrum")




fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
line1, = ax1.plot(np.abs(pluto.rx()))
line2, = ax2.plot(np.abs(np.fft.fft(pluto.rx())))

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def update_signal():
    signal = np.abs(pluto.rx())
    line1.set_ydata(signal)
    line2.set_ydata(np.abs(np.fft.fft(signal)))
    canvas.draw()
    root.after(50, update_signal)

update_signal()
root.mainloop()

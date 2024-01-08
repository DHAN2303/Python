import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        # Left frame
        left_frame = tk.Frame(self)
        left_frame.pack(side="left", fill="y")

        # Label and button
        tk.Label(left_frame, text="Left").pack()
        tk.Button(left_frame, text="Button").pack()

        # Scrollbar
        left_scroll = tk.Scrollbar(left_frame, orient="vertical")
        left_scroll.pack(side="right", fill="y")

        # Center frame
        center_frame = tk.Frame(self)
        center_frame.pack(fill="both", expand=True)

        # Sin wave
        sin_wave = np.sin(np.linspace(0, 2 * np.pi, 100))
        fig, (ax1, ax2) = plt.subplots(2, 1)
        ax1.plot(sin_wave)
        ax1.set_title("Sin Wave")
        ax2.plot(np.abs(np.fft.fft(sin_wave)))
        ax2.set_title("Spectrum")
        canvas = FigureCanvasTkAgg(fig, center_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

        # Right frame
        right_frame = tk.Frame(self)

        # Label and button
        tk.Label(right_frame, text="Right").pack()
        tk.Button(right_frame, text="Button").pack()

        # Scrollbar
        right_scroll = tk.Scrollbar(right_frame, orient="vertical")
        right_scroll.pack(side="right", fill="y")
        right_frame.pack(side="right", fill="y")


root = tk.Tk()
app = Application(master=root)
app.mainloop()

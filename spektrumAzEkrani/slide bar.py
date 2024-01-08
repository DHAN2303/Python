from tkinter import *

# master = Tk()
#
# w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
# w.pack()
#
# mainloop()

# def show_values():
#     print (w1.get(), w2.get())
#
# master = Tk()
# w1 = Scale(master, from_=0, to=42)
# w1.pack()
# w2 = Scale(master, from_=0, to=200, orient=HORIZONTAL)
# w2.pack()
# Button(master, text='Show', command=show_values).pack()
#
# mainloop()

# def show_values():
#     print (w1.get(), w2.get())
#
# master = Tk()
# w1 = Scale(master, from_=0, to=42)
# w1.set(19)
# w1.pack()
# w2 = Scale(master, from_=0, to=200, orient=HORIZONTAL)
# w2.set(23)
# w2.pack()
# Button(master, text='Show', command=show_values).pack()
#
# mainloop()

# def show_values():
#     print (w1.get(), w2.get())
#
# master = Tk()
# w1 = Scale(master, from_=0, to=42, tickinterval=10)
# w1.set(19)
# w1.pack()
# # w2 = Scale(master, from_=0, to=200,tickinterval=50, orient=HORIZONTAL)
# w2 = Scale(master, from_=0, to=200, length=600,tickinterval=10, orient=HORIZONTAL)
# w2.set(23)
# w2.pack()
# Button(master, text='Show', command=show_values).pack()
#
# mainloop()

# import tkinter as tk
#
# def change_position(value):
#     slide_bar.set(value)
#
# root = tk.Tk()
#
# slide_bar = tk.Scale(root, from_=0, to=100, orient='horizontal', command=change_position)
# slide_bar.pack()
#
# entry = tk.Entry(root)
# entry.pack()
#
# button = tk.Button(root, text='Set Position', command=lambda: change_position(int(entry.get())))
# button.pack()
#
# root.mainloop()
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
canvas = tk.Canvas(win)
frame = tk.Frame(canvas)

scroll = ttk.Scrollbar(win, orient='vertical', command=canvas.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scroll.set)
canvas.pack(fill=tk.BOTH, expand=1)
canvas.create_window((0, 0), window=frame, anchor='nw')

for _ in range(30):

    tk.Label(frame, text="big label").pack(pady=20)

win.mainloop()
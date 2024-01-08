# import tkinter as tk
# from tkinter import ttk
# #
# root = tk.Tk()
# root.resizable(False, False)
# # root.title("Scrollbar Widget Example")
# #
# # # apply the grid layout
# # root.grid_columnconfigure(0, weight=1)
# # root.grid_rowconfigure(0, weight=1)
# #
# # # create the text widget
# # text = tk.Text(root, height=10)
# # text.grid(row=0, column=0, sticky=tk.EW)
# #
# # # create a scrollbar widget and set its command to the text widget
# # scrollbar = ttk.Scrollbar(root, orient='vertical')
# # scrollbar.grid(row=0, column=1, sticky=tk.NS)
# #
# # #  communicate back to the scrollbar
# # text['yscrollcommand'] = scrollbar.set
# #
# # # add sample text to the text widget to show the screen
# # for i in range(1,50):
# #     position = f'{i}.0'
# #     text.insert(position,f'Line {i}\n');
# #
# # root.mainloop()
#
# import tkinter as tk
#
# # Create a new tkinter window
# root = tk.Tk()
# root.title("Spectrum Analyzer")
#
# # Create a frame for the left side of the screen
# left_frame = tk.Frame(root)
# left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#
# # Add a canvas widget to the left frame
# left_canvas = tk.Canvas(left_frame)
# left_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#
# # Add a scrollbar widget to the left frame and connect it to the canvas
# left_scrollbar = tk.Scrollbar(left_frame, orient="vertical", command=left_canvas.yview)
# left_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# left_canvas.configure(yscrollcommand=left_scrollbar.set)
#
# # Create a frame inside the canvas to hold the widgets
# left_inner_frame = tk.Frame(left_canvas)
# left_canvas.create_window((0, 0), window=left_inner_frame, anchor="nw")
# kazancAyarlari7 = tk.Label(left_inner_frame, text="Kazanç (dB)").pack(side="top", fill="both", expand=True)
# kazancAyarlari73 = tk.Label(left_inner_frame, text="Kazanç (dB)").pack(side="top", fill="both", expand=True)
# kazancAyarlari723 = tk.Label(left_inner_frame, text="Kazanç (dB)").pack(side="top", fill="both", expand=True)
# kazancAyarlari732 = tk.Label(left_inner_frame, text="Kazanç (dB)").pack(side="top", fill="both", expand=True)
# kazancAyarlari753= tk.Label(left_inner_frame, text="Kazanç (dB)").pack(side="top", fill="both", expand=True)
# kazancAyarlari756 = tk.Label(left_inner_frame, text="Kazanç (dB)").pack(side="top", fill="both", expand=True)
# kazancAyarlari7533 = tk.Label(left_inner_frame, text="Kazanç (dB)").pack(side="top", fill="both", expand=True)
# kazancAyarlari763 = tk.Label(left_inner_frame, text="Kazanç (dB)").pack(side="top", fill="both", expand=True)
# kazancAyarlari764 = tk.Label(left_inner_frame, text="Kazanç (dB)").pack(side="top", fill="both", expand=True)
# kazancAyarlari7757 = tk.Label(left_inner_frame, text="Kazanç (dB)").pack(side="top", fill="both", expand=True)
#
#
# # add other widgets in the inner frame
#
# # Add function to update the scrollregion
# def update_scrollregion(event):
#     left_canvas.configure(scrollregion=left_canvas.bbox("all"))
#
# left_inner_frame.bind("<Configure>", update_scrollregion)
#
# root.mainloop()

# Import the required libraries

# from tkinter import *
#
# root = Tk()
# root.title('Buttons')
# f = Frame(root, width=300, height=110)
# xf = Frame(f, relief=GROOVE, borderwidth=2)
# Label(xf, text="AAA").pack(pady=10)
# Button(xf, text="bbb", state=DISABLED).pack(side=LEFT, padx=5, pady=8)
# Button(xf, text="ccc rrr rrr rrr rrr", command=root.quit).pack(side=RIGHT, padx=5, pady=8)
# xf.place(relx=0.01, rely=0.125, anchor=NW)
# Label(f, text='Titled Border').place(relx=.06, rely=0.125,anchor=W)
# f.pack()
# root.mainloop()

# Import the required libraries
from tkinter import *
from PIL import ImageTk, Image

# Create an instance of Tkinter Frame
win = Tk()

# Set the geometry of Tkinter Frame
win.geometry("700x450")

# Open the Image File
bg = ImageTk.PhotoImage(file="")

# Create a Canvas
canvas = Canvas(win, width=700, height=3500)
canvas.pack(fill=BOTH, expand=True)

# Add Image inside the Canvas
canvas.create_image(0, 0, image=bg, anchor='nw')

# Function to resize the window
def resize_image(e):
   global image, resized, image2
   # open image to resize it
   image = Image.open("1.png")
   # resize the image with width and height of root
   resized = image.resize((e.width, e.height), Image.ANTIALIAS)

   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(0, 0, image=image2, anchor='nw')

# Bind the function to configure the parent window
win.bind("<Configure>", resize_image)
win.mainloop()



import tkinter as tk

# Create a new tkinter window
root = tk.Tk()
root.title("Spectrum Analyzer")

# Create a frame for the left side of the screen
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a frame for the first menu
menu1_frame = tk.Frame(left_frame)
menu1_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create a frame for the second menu
menu2_frame = tk.Frame(left_frame)
menu2_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Add widgets to the menu frames

# Create a button to switch between the menus
menu_button = tk.Button(left_frame, text="Switch Menu", command=lambda: switch_menu())
menu_button.pack(side=tk.BOTTOM)

# Create a variable to keep track of the current menu
current_menu = 1

# Create a function to switch between the menus
def switch_menu():
    global current_menu
    if current_menu == 1:
        menu1_frame.pack_forget()
        menu2_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        current_menu = 2
    else:
        menu2_frame.pack_forget()
        menu1_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        current_menu = 1

root.mainloop()

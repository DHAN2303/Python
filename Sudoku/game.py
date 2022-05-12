from tkinter import *
from tkinter import ttk

sudoku = Tk()
sudoku.title('Sudoku')

second = 0
minute = 0
hour = 0

Label(sudoku, text='CLICK GENERATE, FILL IN THE NUMBERS AND CLICK SOLVE', font=("Arial", 20, "bold"),
                    bg='#EEC900', width=88, fg='black').grid(row=0, column=0, columnspan=10)

def only_one_numbers(char,):
        return char.isdigit()
validation = sudoku.register(only_one_numbers)

#========================================= Create the grid according to the Mode ====================================

def Easy():
    for widget in sudoku.winfo_children():
        widget.destroy()
        Label(sudoku, text='CLICK GENERATE, FILL IN THE NUMBERS AND CLICK SOLVE', font=("Arial", 20, "bold"),
              bg='#EEC900', width=88, fg='black').grid(row=0, column=0, columnspan=10)
        gameMode()
        buttons()
        # timer()

    for rows in range(1, 4):
        for columns in range(1, 4):
            if rows in (1,2,3) and columns == 2:
                kleur='azure4'
            else:
                kleur = 'azure2'

            cell = Frame(sudoku, highlightthickness=1, highlightcolor='blue', highlightbackground='cornsilk4')
            cell.grid(row=rows, column=columns,columnspan=6)
            Entry(cell,bg=kleur, width=3, font=("Arial", 60, "bold"), fg='black',
                      validate="key", validatecommand=(validation, '%S'), ).pack()


def Normal():
    [widget.delete(0, END) for widget in sudoku.winfo_children() if isinstance(widget, Entry)]

    for rows in range(1, 7):
        for columns in range(1, 7):
            if rows in (1,2,3,4,5,6) and columns in (3,4):
                kleur='azure4'
            else:
                kleur = 'azure2'

            cell = Frame(sudoku, highlightthickness=1, highlightcolor='blue', highlightbackground='cornsilk4')
            cell.grid(row=rows, column=columns,columnspan=2)
            Entry(cell,bg=kleur, width=3, font=("Arial", 60, "bold"), fg='black',
                      validate="key", validatecommand=(validation, '%S'), ).pack()


def Hard():
    for widget in sudoku.winfo_children():
        widget.destroy()
        Label(sudoku, text='CLICK GENERATE, FILL IN THE NUMBERS AND CLICK SOLVE', font=("Arial", 20, "bold"),
              bg='#EEC900', width=88, fg='black').grid(row=0, column=0, columnspan=10)
        gameMode()
        buttons()
        # timer()

    for rows in range(1, 10):
        for columns in range(1, 10):
            if ((rows in (1,2,3,7,8,9) and columns in (4,5,6)) or (rows in (4,5,6) and columns in (1,2,3,7,8,9))):
                kleur='azure4'
            else:
                kleur = 'azure2'
            cell = Frame(sudoku, highlightthickness=1, highlightcolor='blue', highlightbackground='cornsilk4')
            cell.grid(row=rows, column=columns)
            Entry(cell, bg=kleur, width=3, font=("Arial", 60, "bold"), fg='black',
                      validate="key", validatecommand=(validation, '%S'), ).pack()

#================================= Create the functions for buttons=========================

def clear():
    for widget in sudoku.winfo_children():
        widget.destroy()
        Label(sudoku, text='CLICK GENERATE, FILL IN THE NUMBERS AND CLICK SOLVE', font=("Arial", 20, "bold"),
              bg='#EEC900', width=88, fg='black').grid(row=0, column=0, columnspan=10)
        gameMode()
        buttons()

def solve():
    return

def backPage():

    return

def generate():
    return

# ======================================Create the buttons============================
def buttons():
    buttonsFrame = LabelFrame(sudoku, foreground="black", bg='#EEC900')
    buttonsFrame.grid(row=14, column=6, columnspan=5)
    Button(buttonsFrame, text='Clear', command=clear, width=5, height=2).grid(row=13, column=6)
    Button(buttonsFrame, text='Solve', command=solve, width=5, height=2).grid(row=13, column=7)
    Button(buttonsFrame, text='Generate', command=generate, width=5, height=2).grid(row=13, column=8)
    Button(buttonsFrame, text='Go back', command=backPage, width=5, height=2).grid(row=13, column=9)
    exitbutton = Button(buttonsFrame, text='Exit', width=32, height=2, command=sudoku.destroy)
    exitbutton.grid(row=15, column=6, columnspan=6)

buttons()
# ===================================GAME MODES=================================
def gameMode():
    MODE = LabelFrame(sudoku, text='PLAY MODE', font=("Arial", 10,), bg='#EEC900', bd=4, foreground="black")
    MODE.grid(row=14, column=0, columnspan=5)
    easy = Button(MODE, text="Easy", command=Easy, width=7, height=2).grid(row=1, column=1)
    normal = Button(MODE, text="Normal", command=Normal, width=7,height=2).grid(row=1, column=2)
    hard = Button(MODE, text="Hard", command=Hard,width=7, height=2).grid(row=1, column=3)

gameMode()

# ========================================================= counter and score ========================================

# def timer():
#     label = Label(sudoku, fg="#EEC900", font=("Arial", 20, "bold"),width=20)
#     label.grid(row=14, column=2, columnspan=5)
#     def counter(label):
#         second = 0
#         minute = 0
#         hour = 0
#         def count():
#             global second, hour, minute
#             second += 1
#             if second == 60:
#                 minute = minute + 1
#                 if minute == 60:
#                     hour = hour + 1
#                     minute = 0
#                 second = 0
#             label.config(text=f'Your time: {hour}:{minute}:{second}')
#             label.after(1000, count)
#         count()
#     counter(label)

sudoku.mainloop()
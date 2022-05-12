from tkinter import *
from tkinter import ttk

sudoku = Tk()
sudoku.title('Sudoku')


mylabel = Label(sudoku, text='CLICK GENERATE, FILL IN THE NUMBERS AND CLICK SOLVE',font=("Arial", 20, "bold"),bg='#EEC900',width=88,fg='black').grid(row=0, column=0,columnspan=10)

def only_one_numbers(char,):

        return char.isdigit()

validation = sudoku.register(only_one_numbers)


# Create the grid
def beg():
    cells = {}
    for row in range(1, 10):
        for column in range(1, 10):
            if ((row in (1,2,3,7,8,9) and column in (4,5,6)) or (row in (4,5,6) and column in (1,2,3,7,8,9))):
                kleur='azure4'
            else:
                kleur = 'azure2'

            cell = Frame(sudoku, highlightthickness=1, highlightcolor='blue', highlightbackground='cornsilk4')
            cell.grid(row=row, column=column)
            cells[(row, column)] = cell
            e = Entry(cells[row, column], bg=kleur, width=3, font=("Arial", 60, "bold"), fg='black',
                      validate="key", validatecommand=(validation, '%S'), )
            e.pack()
            print(e)





beg()
# Create the functions for buttons
def clear():
    return


def solve():
    return

def generate():
    return
#     for i in range(len(cells)):
#         for j in range(len(cells[i])):
#             cells[i][j] = 0
#
#     label_number = easysudoku.nametowidget('number')
#     number = label_number['text']
#
#     numbers_generated = 0
#
#     while numbers_generated < number:  # weil es von 0 zu zählen beginnt!
#         num = random.randint(1, 9)
#         paste_row = random.randint(0, 8)  # i know thats not really professional or scalable
#         paste_col = random.randint(0, 8)
#         test = valid(bord=sudoku, row=paste_row, col=paste_col, num=num)
#         if test:
#             sudoku[paste_row][paste_col] = num
#             print( str(numbers_generated) + ': ' +str(num) + ' generated on ' + str(paste_col) + ':' + str(paste_row))
#             numbers_generated += 1
#         print(str(numbers_generated) + ' numbers generated')
#
#     placeBoard()
#     solve(bord=sudoku)
#
#     for i in sudoku:
#         print(i)
#     print('')


def Easy():
    print('1')
def Normal():
    print('2')
def Hard():
    print('3')

# Create the buttons
clearer = Button(sudoku, text='Clear', command=clear,width=9).grid(row=13, column=6,columnspan=1, pady=30,rowspan=3)
solver = Button(sudoku, text='Solve', command=solve,width=9).grid(row=13, column=7,columnspan=1, pady=30,rowspan=3)
genera = Button(sudoku, text='Generate', command=generate,width=9).grid(row=13, column=8,columnspan=1, pady=30,rowspan=3)

# GAME MODES
gamemode = Label(text='       Play Mode :',font=("Arial", 15,)).grid(row=14,column=1)
Checkbuttonmode = IntVar()
easy = Checkbutton(sudoku, text="Easy",command=Easy, variable =Checkbuttonmode, width=7, height=2,onvalue = 1, offvalue = 0).grid(row=14, column=1,columnspan=3)
normal = Checkbutton(sudoku, text="Normal",command=Normal,variable = Checkbuttonmode, width=7, height=2,onvalue = 2, offvalue = 3).grid(row=14, column=3,columnspan=1)
hard = Checkbutton(sudoku, text="Hard",command=Hard,variable = Checkbuttonmode, width=7, height=2,onvalue = 4, offvalue = 5).grid(row=14, column=4,columnspan=1)


sudoku.mainloop()
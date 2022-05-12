import random
from tkinter import *
import time

sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def valid(bord, row, col, num):
    # pos_x = col
    # pos_y = row
    # num = number that we are trying to insert

    # check row
    if bord[row][col] != 0:
        return False
    else:
        if num in bord[row]:
            return False

        # check col
        for i in range(len(bord)):
            if bord[i][col] == num:
                return False

        cube_x = col // 3  # Integer-Division (rundet): da kommt dann entweder 0, 1 oder 2 für die Spalte!
        cube_y = row // 3  # Integer-Division (rundet): da kommt dann entweder 0, 1 oder 2 für die Reihe!

        for i in range(cube_y * 3, cube_y * 3 + 3):
            for j in range(cube_x * 3, cube_x * 3 + 3):
                if bord[i][j] == num:
                    return False

        return True


def find(bord):
    for i in range(len(bord)):  # Länge der Reihe
        for j in range(len(bord[0])):  # Länge der Spalte
            if bord[i][j] == 0:
                return (i, j)


def solve(bord):
    empty = find(bord=bord)

    if not empty:
        return True  # dann sind wir fertig!
    else:
        row, col = empty

    for num in range(1, 10):  # 1-9
        # position = str(row) +  "-" + str(col)
        # lb = root.nametowidget(position)

        if valid(bord=bord, row=row, col=col, num=num):
            bord[row][col] = num
            # lb.after(0, lambda: lb.config(bg='green', text=str(num)))

            if solve(bord):  # BACKTRACKING - recursively (RÜCKWÄRTS!)
                return True
            else:
                # lb.after(0, lambda: lb.config(bg='red', text=str(num)))
                bord[row][col] = 0  # reset

    # time.sleep(0.0001)

    return False


def print_board(board):
    for i in board:
        print(i)


def placeBoard():
    y = 0

    for i in range(len(sudoku)):
        x = 0

        if i % 3 == 0 and i != 0:
            display_lab = Label(root, text="  ", bg='gainsboro')
            display_lab.grid(row=y, column=0)
            y += 1

        for j in range(len(sudoku[i])):

            if j % 3 == 0 and j != 0:
                display_lab = Label(root, text="  ", bg='gainsboro')  # heller Abstand zwischen den 9x9 Feldern
                display_lab.grid(row=0, column=x)
                x += 1
            if j == 10:
                x = 10
            name = str(i) + '-' + str(j)

            num = sudoku[i][j]
            if num == 0:

                display_lab = Label(root, text="  ", bg='yellow', name=name)  # for row and col

            else:
                display_lab = Label(root, text=num, bg='white', name=name,fg='red')  # for row and col

            display_lab.grid(row=y, column=x)
            # display_lab.config(bg='grey')

            x += 1
        y += 1


# lb = Label(root, text='hello guys', name='guys')
# lb.grid(row=10, column=10)


# root.nametowidget(".0-9")

def generate_sudoku():
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            sudoku[i][j] = 0

    label_number = root.nametowidget('number')
    number = label_number['text']

    numbers_generated = 0

    while numbers_generated < number:  # weil es von 0 zu zählen beginnt!
        num = random.randint(1, 9)
        paste_row = random.randint(0, 8)  # i know thats not really professional or scalable
        paste_col = random.randint(0, 8)
        test = valid(bord=sudoku, row=paste_row, col=paste_col, num=num)
        if test:
            sudoku[paste_row][paste_col] = num
            # print( str(numbers_generated) + ': ' +str(num) + ' generated on ' + str(paste_col) + ':' + str(paste_row))
            numbers_generated += 1
        # print(str(numbers_generated) + ' numbers generated')

    placeBoard()
    solve(bord=sudoku)

    for i in sudoku:
        print(i)
    print('')


def plusNumber():
    label_number = root.nametowidget('number')
    text = label_number['text']
    if text < 15:
        label_number.config(text=text + 1)


def minusNumber():
    label_number = root.nametowidget('number')
    text = label_number['text']
    if text > 1:
        label_number.config(text=text - 1)


def blink():  # test function for changes with button
    lb.config(bg='green')
    lb.after(3000, lambda: lb.config(bg='white'))


root = Tk()
root.title('Sudoku')

placeBoard()

# print_board(sudoku)

position = "0-8"
lb = root.nametowidget(position)

# print_board(sudoku)


b2 = Button(root, text="+", command=plusNumber)
b3 = Button(root, text="-", command=minusNumber)
b2.grid(row=12, column=12)
b3.grid(row=13, column=12)

lb = Label(root, text=8, bg='grey', name="number")
lb.grid(row=12, column=13)

b4 = Button(root, text="Generate", command=generate_sudoku, bg='yellow')
b4.grid(row=12, column=14)

b = Button(root, text="Solve!", command=placeBoard, bg='green')
b.grid(row=13, column=14)

root.mainloop()
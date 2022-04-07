import tkinter as t
from tkinter import TOP, RIGHT
import re
clc = t.Tk()
clc.title('Calculator')

def click(num):
    global expression

    expression = expression + str(num)

    input.set(expression)

def clear():
    global expression

    expression = ""

    input.set("")

def equal():
    global expression

    result = str(eval(expression))

    input.set(result)

    expression = result

expression = ""

input = t.StringVar()

input_frame = t.Frame(clc, width=312, height=50, bd=0)
input_frame.pack(side=TOP)

input_field = t.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input, width=44, bg="black", justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

frame = t.Frame(clc, width=312, height=272.5, bg="grey")
frame.pack()

c = t.Button(frame, text="C", fg="black", width=37, height=3, bg="black", command=lambda: clear())
c.grid(row=0, column=0, columnspan=3)

divide = t.Button(frame, text="/", fg="black", width=10, height=3, bg="black",command=lambda: click("/"))
divide.grid(row=0, column=3)

seven = t.Button(frame, text="7", fg="black", width=10, height=3, bg="black",command=lambda: click(7))
seven.grid(row=1, column=0)

eight = t.Button(frame, text="8", fg="black", width=10, height=3, bg="black", command=lambda: click(8))
eight.grid(row=1, column=1)

nine = t.Button(frame, text="9", fg="black", width=10, height=3, bg="black", command=lambda: click(9))
nine.grid(row=1, column=2)

multiply = t.Button(frame, text="*", fg="black", width=10, height=3, bg="black", command=lambda: click("*"))
multiply.grid(row=1, column=3)

four = t.Button(frame, text="4", fg="black", width=10, height=3, bg="black", command=lambda: click(4))
four.grid(row=2, column=0)

five = t.Button(frame, text="5", fg="black", width=10, height=3, bg="black", command=lambda: click(5))
five.grid(row=2, column=1)

six = t.Button(frame, text="6", fg="black", width=10, height=3, bg="black", command=lambda: click(6))
six.grid(row=2, column=2)

minus = t.Button(frame, text="-", fg="black", width=10, height=3, bg="black", command=lambda: click("-"))
minus.grid(row=2, column=3)

one = t.Button(frame, text="1", fg="black", width=10, height=3, bg="black", command=lambda: click(1))
one.grid(row=3, column=0)

two = t.Button(frame, text="2", fg="black", width=10, height=3, bg="black", command=lambda: click(2))
two.grid(row=3, column=1)

three = t.Button(frame, text="3", fg="black", width=10, height=3, bg="black", command=lambda: click(3))
three.grid(row=3, column=2)

plus = t.Button(frame, text="+", fg="black", width=10, height=3, bg="black", command=lambda: click("+"))
plus.grid(row=3, column=3)

zero= t.Button(frame, text="0", fg="black", width=10, height=3, bg="black", command=lambda: click(0))
zero.grid(row=4, column=0)

ex = t.Button(frame, text="^", fg="black", width=10, height=3, bg="black", command=lambda: click("**"))
ex.grid(row=4, column=1)

point= t.Button(frame, text=".", fg="black", width=10, height=3, bg="black", command=lambda: click("."))
point.grid(row=4, column=2)

equals= t.Button(frame, text="=", fg="black", width=10, height=3, bg="black", command=lambda: equal())
equals.grid(row=4, column=3)

clc.mainloop()
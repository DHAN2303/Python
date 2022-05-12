from tkinter import *
from tkinter import ttk


def save_player_info():
    player_info = playerName.get()

    if player_info == '':
        return Label(sudokumain,text='Please Write Your Name',width=50,fg='firebrick2',font=("Arial", 15, "bold")).grid(row=6, column=0,columnspan=2)

    file = open("user.txt", "a")
    file.write(player_info)
    file.write("\n")
    file.close()

def exit():
    return

def leaderboard1():
    # leaderboard

    Label(sudokumain, text='★★★★★★LEADERBOARD★★★★★★\nTHE BEST TIME WASTER IN THE WORLD',
                             bg="#EEC900", width=100, fg='black', font=("Arial", 15, "bold")).grid(row=1, column=0,
                                                                                                  columnspan=2)

    leaderboard = ttk.Treeview(sudokumain, column=("c1", "c2", "c3","c4"), show='headings', height=10)
    leaderboard.grid(row=2, column=0, columnspan=2)
    leaderboard.column("# 1", anchor=CENTER,width=225,)
    leaderboard.heading("# 1", text="ID")
    leaderboard.column("# 2", anchor=CENTER,width=225,)
    leaderboard.heading("# 2", text="Player Name")
    leaderboard.column("# 3", anchor=CENTER,width=225,)
    leaderboard.heading("# 3", text="Score")
    leaderboard.column("# 4", anchor=CENTER, width=225, )
    leaderboard.heading("# 4", text="Time")

    f = open("user.txt", "r")
    i = 0
    for x in f:
        i = i + 1
        leaderboard.insert('', END, text="1", values=(i, x, ''))
    f.close()

    # number of players
    Label(text=f"Number of Players: {i}", bg="#EEC900", width=100, fg='black',
                    font=("Arial", 15, "bold")).grid(row=3, column=0, columnspan=2)


sudokumain = Tk()
sudokumain.title('CHINESE SUDOKU')
# welcome
wellcomelabel = Label(text='WELLCOME TO THE CHEAPEST SUDOKU GAME IN THE WORLD', fg="black", bg="yellow",width=100, height=3, font=10).grid(row=0, column=0, columnspan=10)

leaderboard1()

# PLAYER NAME
playerNamel = Label(sudokumain,text="Your Name :",font=("Helvetica", 15),pady=20).grid(row=4, column=0,columnspan=1)
playerName = StringVar()
playerName_entry = Entry(sudokumain,textvariable=playerName, width=50,justify='center',bd =3,fg='red' ).grid(row=4, column=1,columnspan=2)

# buttons
STARTbutton = Button(sudokumain, text="Let's Play", command=save_player_info, width=20, height="1",activeforeground='green',font=("Helvetica", 20, "bold"),pady=5)
STARTbutton.grid(row=5, column=0,columnspan=1)
Exitbutton = Button(sudokumain, text="EXIT",command=lambda :sudokumain.destroy(), width=20, height="1",activeforeground='red',font=("Helvetica", 20, "bold"),pady=5)
Exitbutton.grid(row=5, column=1,columnspan=2)

sudokumain.mainloop()
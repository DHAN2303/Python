import tkinter as tk
from tkinter import ttk, CENTER, END

class sudokuApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Chinese Sudoku')

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.frames = {}

        for F in (StartPage, hard, easy, normal):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self,text='WELLCOME TO THE CHEAPEST SUDOKU GAME IN THE WORLD', fg="black", bg="yellow",
                 width=100, height=3, font=10).grid(row=0, column=0, columnspan=10)
        self.playerName = tk.StringVar()

        def save_player_info():
            player_info = self.playerName.get()
            if player_info == '':
                error = tk.Label(self, text='Please Write Your Name', width=50, fg='firebrick2',
                                 font=("Arial", 15, "bold"))
                error.grid(row=6, column=0, columnspan=2)
                return error
            file = open("user.txt", "a")
            file.write(player_info)
            file.write("\n")
            file.close()
            for widget in self.winfo_children():
                if isinstance(widget, tk.Entry):
                    widget.delete(0, tk.END)
            controller.show_frame(easy)

        # leaderbord
        def leaderboard1(self):
            # leaderboard

            tk.Label(self, text='★★★★★★LEADERBOARD★★★★★★\nTHE BEST TIME WASTER IN THE WORLD',
                     bg="#EEC900", width=100, fg='black', font=("Arial", 15, "bold")).grid(row=1, column=0,
                                                                                           columnspan=2)

            leaderboard = ttk.Treeview(self, column=("c1", "c2", "c3", "c4"), show='headings', height=10)
            leaderboard.grid(row=2, column=0, columnspan=2)
            leaderboard.column("# 1", anchor=CENTER, width=225, )
            leaderboard.heading("# 1", text="ID")
            leaderboard.column("# 2", anchor=CENTER, width=225, )
            leaderboard.heading("# 2", text="Player Name")
            leaderboard.column("# 3", anchor=CENTER, width=225, )
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
            tk.Label(self,text=f"Number of Players: {i}", bg="#EEC900", width=100, fg='black',
                     font=("Arial", 15, "bold")).grid(row=3, column=0, columnspan=2)

        leaderboard1(self)
        # PLAYER NAME
        tk.Label(self, text="Your Name :", font=("Helvetica", 15), pady=20).grid(row=4, column=0,
                                                                                 columnspan=1)

        playername = tk.Entry(self, textvariable=self.playerName, width=50, justify='center', bd=3, fg='red')
        playername.grid(row=4, column=1, columnspan=2)

        # buttons
        STARTbutton = tk.Button(self, text="Let's Play", command=save_player_info, width=20, height="1",
                                activeforeground='green', font=("Helvetica", 20, "bold"), pady=5)
        STARTbutton.grid(row=5, column=0, columnspan=1)
        Exitbutton = tk.Button(self, text="EXIT", command=lambda: self.quit(), width=20, height="1",
                               activeforeground='red', font=("Helvetica", 20, "bold"), pady=5)
        Exitbutton.grid(row=5, column=1, columnspan=2)

class easy(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text='CLICK GENERATE, FILL IN THE NUMBERS AND CLICK SOLVE', font=("Arial", 20, "bold"),
                 bg='#EEC900', width=88, fg='black').grid(row=0, column=0, columnspan=10)

        def only_one_numbers(char):
            return char.isdigit()

        validation = self.register(only_one_numbers)

        for rows in range(1, 4):
            for columns in range(1, 4):
                if rows in (1, 2, 3) and columns == 2:
                    kleur = 'azure4'
                else:
                    kleur = 'azure2'

                tk.Entry(self, bg=kleur, width=3, font=("Arial", 60, "bold"), fg='black',
                         validate="key", validatecommand=(validation, '%S'), ).grid(row=rows, column=columns,
                                                                                    columnspan=6)

        # ================================= Create the functions for buttons=========================

        def clear():
            for widget in self.winfo_children():
                if isinstance(widget, tk.Entry):
                    widget.delete(0, tk.END)

        def solve():
            return

        def easyLavel():
            for widget in self.winfo_children():
                if isinstance(widget, tk.Entry):
                    widget.delete(0, tk.END)
            controller.show_frame(easy)

        def normalLavel():
            for widget in self.winfo_children():
                if isinstance(widget, tk.Entry):
                    widget.delete(0, tk.END)
            controller.show_frame(normal)

        def hardLavel():
            for widget in self.winfo_children():
                if isinstance(widget, tk.Entry):
                    widget.delete(0, tk.END)
            controller.show_frame(hard)

        # ======================================Create the buttons============================
        def buttons(self):
            buttonsFrame = tk.LabelFrame(self, foreground="black", bg='#EEC900')
            buttonsFrame.grid(row=14, column=6, columnspan=5)
            tk.Button(buttonsFrame, text='Clear', command=clear, activeforeground='red', width=5, height=2).grid(row=13,
                                                                                                                 column=6)
            tk.Button(buttonsFrame, text='Solve', command=solve, width=5, height=2).grid(row=13, column=7)
            exitbutton = tk.Button(buttonsFrame, text='Exit', activeforeground='red', width=15, height=2,
                                   command=lambda: controller.show_frame(StartPage))
            exitbutton.grid(row=13, column=8, columnspan=6)

        buttons(self)

        # ===================================GAME MODES=================================
        def gameMode(self):
            MODE = tk.LabelFrame(self, text='PLAY MODE', font=("Arial", 10,), bg='#EEC900', bd=4, foreground="black")
            MODE.grid(row=14, column=0, columnspan=5)
            tk.Button(MODE, text="Easy mode\n Generate", fg='blue', command=easyLavel, width=7, height=2).grid(row=1,
                                                                                                               column=1)
            tk.Button(MODE, text="Normal mode\n Generate", fg='green', command=normalLavel, width=7, height=2).grid(
                row=1, column=2)
            tk.Button(MODE, text="Hard mode\n Generate", fg='red', width=7, command=hardLavel, height=2).grid(row=1,
                                                                                                              column=3)

        gameMode(self)

class normal(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text='CLICK GENERATE, FILL IN THE NUMBERS AND CLICK SOLVE', font=("Arial", 20, "bold"),
                 bg='#EEC900', width=88, fg='black').grid(row=0, column=0, columnspan=10)

        def only_one_numbers(char):
            return char.isdigit()

        validation = self.register(only_one_numbers)

        for rows in range(1, 7):
            for columns in range(1, 7):
                if rows in (1, 2, 3, 4, 5, 6) and columns in (3, 4):
                    kleur = 'azure4'
                else:
                    kleur = 'azure2'

                tk.Entry(self, bg=kleur,width=3, font=("Arial", 60, "bold"), fg='black',
                      validate="key", validatecommand=(validation, '%S'), ).grid(row=rows, column=columns, columnspan=2)

        # ================================= Create the functions for buttons=========================

        def clear():
            for widget in self.winfo_children():
                if isinstance(widget, tk.Entry):
                    widget.delete(0, tk.END)


        def solve():
            return

        def easyLavel():
            for widget in self.winfo_children():
                if isinstance(widget, tk.Entry):
                    widget.delete(0, tk.END)
            controller.show_frame(easy)

        def normalLavel():
            for widget in self.winfo_children():
                if isinstance(widget, tk.Entry):
                    widget.delete(0, tk.END)
            controller.show_frame(normal)

        def hardLavel():
            for widget in self.winfo_children():
                if isinstance(widget, tk.Entry):
                    widget.delete(0, tk.END)
            controller.show_frame(hard)

        # ======================================Create the buttons============================
        def buttons(self):
            buttonsFrame = tk.LabelFrame(self, foreground="black", bg='#EEC900')
            buttonsFrame.grid(row=14, column=6, columnspan=5)
            tk.Button(buttonsFrame, text='Clear', command=clear, activeforeground='red', width=5, height=2).grid(row=13,
                                                                                                                 column=6)
            tk.Button(buttonsFrame, text='Solve', command=solve, width=5, height=2).grid(row=13, column=7)
            exitbutton = tk.Button(buttonsFrame, text='Exit', activeforeground='red', width=15, height=2,
                                   command=lambda: controller.show_frame(StartPage))
            exitbutton.grid(row=13, column=8, columnspan=6)

        buttons(self)

        # ===================================GAME MODES=================================
        def gameMode(self):
            MODE = tk.LabelFrame(self, text='PLAY MODE', font=("Arial", 10,), bg='#EEC900', bd=4, foreground="black")
            MODE.grid(row=14, column=0, columnspan=5)
            tk.Button(MODE, text="Easy mode\n Generate",fg='blue',command=easyLavel, width=7, height=2).grid(row=1, column=1)
            tk.Button(MODE, text="Normal mode\n Generate",fg='green',command=normalLavel, width=7, height=2).grid(row=1, column=2)
            tk.Button(MODE, text="Hard mode\n Generate",fg='red', width=7,command=hardLavel, height=2).grid(row=1, column=3)
        gameMode(self)

class hard(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text='CLICK GENERATE, FILL IN THE NUMBERS AND CLICK SOLVE', font=("Arial", 20, "bold"),
              bg='#EEC900', width=88, fg='black').grid(row=0, column=0, columnspan=10)
        def only_one_numbers(char):
            return char.isdigit()

        validation = self.register(only_one_numbers)

        for rows in range(1, 10):
            for columns in range(1, 10):
                if ((rows in (1, 2, 3, 7, 8, 9) and columns in (4, 5, 6)) or (
                        rows in (4, 5, 6) and columns in (1, 2, 3, 7, 8, 9))):
                    kleur = 'azure4'
                else:
                    kleur = 'azure2'
                tk.Entry(self, bg=kleur,width=3, font=("Arial", 60, "bold"), fg='black',
                      validate="key", validatecommand=(validation, '%S'), ).grid(row=rows, column=columns)
        # ================================= Create the functions for buttons=========================

        def clear():
            for widget in self.winfo_children():
                if isinstance(widget, tk.Entry):
                    widget.delete(0, tk.END)

        def solve():
            return

        def easyLavel():
            for widget in self.winfo_children():
                if isinstance(widget, tk.Entry):
                    widget.delete(0, tk.END)
            controller.show_frame(easy)

        def normalLavel():
            for widget in self.winfo_children():
                if isinstance(widget, tk.Entry):
                    widget.delete(0, tk.END)
            controller.show_frame(normal)

        def hardLavel():
            for widget in self.winfo_children():
                if isinstance(widget, tk.Entry):
                    widget.delete(0, tk.END)
            controller.show_frame(hard)



        # ======================================Create the buttons============================
        def buttons(self):
            buttonsFrame = tk.LabelFrame(self, foreground="black", bg='#EEC900')
            buttonsFrame.grid(row=14, column=6, columnspan=5)
            tk.Button(buttonsFrame, text='Clear', command=clear,activeforeground='red', width=5, height=2).grid(row=13, column=6)
            tk.Button(buttonsFrame, text='Solve', command=solve, width=5, height=2).grid(row=13, column=7)
            exitbutton = tk.Button(buttonsFrame, text='Exit',activeforeground='red', width=15, height=2, command=lambda: controller.show_frame(StartPage))
            exitbutton.grid(row=13, column=8, columnspan=6)
        buttons(self)

        # ===================================GAME MODES=================================
        def gameMode(self):
            MODE = tk.LabelFrame(self, text='PLAY MODE', font=("Arial", 10,), bg='#EEC900', bd=4, foreground="black")
            MODE.grid(row=14, column=0, columnspan=5)
            tk.Button(MODE, text="Easy mode\n Generate", fg='blue', command=easyLavel, width=7, height=2).grid(row=1,
                                                                                                               column=1)
            tk.Button(MODE, text="Normal mode\n Generate", fg='green', command=normalLavel, width=7, height=2).grid(
                row=1, column=2)
            tk.Button(MODE, text="Hard mode\n Generate", fg='red', width=7, command=hardLavel, height=2).grid(row=1,
                                                                                                              column=3)

        gameMode(self)


sudokuApp().mainloop()
import tkinter as tk
from tkinter import messagebox

class Game:
    turn = 0 #"0" - randul lui X,, "1" randul lui O
    puncteX = 0 #puncte jucator X
    puncteO = 0 #puncte jucator Y
    winflag = 0 #valoare "1" daca cineva a castigat
    Xwon = 0 #flag if X won
    Owon = 0 #flag if O won
    tie = 0 #flag for ties
    
    def __init__(self, row, col, text):
        self.text = text
        self.image = tk.PhotoImage(width=1, height=1)
        self.btn = tk.Button(game, relief= "flat", bg = "grey", image = self.image, text = " ", font = ("Arial", 100), width = 100, height = 100, compound= "center", command = self.onclick)
        self.btn.grid(row = row, column = col)

    def onclick(self):
        if Game.turn % 2 == 0:
            self.btn.config(bg = "#424242", text = "X", state = "disabled")
            self.text = "X"
            turns()
        else:
            self.btn.config(bg = "#424242", text = "O", state = "disabled")
            self.text = "O"
            turns()
        Game.turn += 1
        if Game.turn > 4:
            wincheck()

    def scor():
        scor.config(text = f"SCOREBOARD:  X: {Game.puncteX}     O: {Game.puncteO}")

def turns():
    if Game.turn < 8:
        if Game.turn % 2 == 0:
            rand.config(text = "Current turn: O")
        else:
            rand.config(text = "Current turn: X")
    else:
        rand.config(text = "TIE")

def reset():
    msg = messagebox.askquestion("Warning", "Reset score?")
    if msg == "yes":
        Game.puncteX = 0
        Game.puncteO = 0
        Game.scor()
    
def wincheck():
    color = "#32CD32" #Winbutton color
    if r1_1.text == r1_2.text == r1_3.text:
        Game.winflag = 1
        r1_1.btn.config(bg = color)
        r1_2.btn.config(bg = color)
        r1_3.btn.config(bg = color)
        if r1_1.text == "X":
            Game.Xwon = 1
            Game.puncteX += 1
            rand.config(text = "X WON")
        else:
            Game.Owon = 1
            Game.puncteO += 1
            rand.config(text = "O WON")
    elif r2_1.text == r2_2.text == r2_3.text:
        Game.winflag = 1
        r2_1.btn.config(bg = color)
        r2_2.btn.config(bg = color)
        r2_3.btn.config(bg = color)
        if r2_1.text == "X":
            Game.Xwon = 1
            Game.puncteX += 1
            rand.config(text = "X WON")
        else:
            Game.Owon =1
            Game.puncteO += 1
            rand.config(text = "O WON")
    elif r3_1.text == r3_2.text == r3_3.text:
        Game.winflag = 1
        r3_1.btn.config(bg = color)
        r3_2.btn.config(bg = color)
        r3_3.btn.config(bg = color)
        if r3_1.text == "X":
            Game.Xwon = 1
            Game.puncteX += 1
            rand.config(text = "X WON")
        else:
            Game.Owon = 1
            Game.puncteO += 1
            rand.config(text = "O WON")
    elif r1_1.text == r2_1.text == r3_1.text:
        Game.winflag = 1
        r1_1.btn.config(bg = color)
        r2_1.btn.config(bg = color)
        r3_1.btn.config(bg = color)
        if r1_1.text == "X":
            Game.Xwon = 1
            Game.puncteX += 1
            rand.config(text = "X WON")
        else:
            Game.Owon = 1
            Game.puncteO += 1
            rand.config(text = "O WON")
    elif r1_2.text == r2_2.text == r3_2.text:
        Game.winflag = 1
        r1_2.btn.config(bg = color)
        r2_2.btn.config(bg = color)
        r3_2.btn.config(bg = color)
        if r1_2.text == "X":
            Game.Xwon = 1
            Game.puncteX += 1
            rand.config(text = "X WON")
        else:
            Game.Owon = 1
            Game.puncteO += 1
            rand.config(text = "O WON")
    elif r1_3.text == r2_3.text == r3_3.text:
        Game.winflag = 1
        r1_3.btn.config(bg = color)
        r2_3.btn.config(bg = color)
        r3_3.btn.config(bg = color)
        if r1_3.text == "X":
            Game.Xwon = 1
            Game.puncteX += 1
            rand.config(text = "X WON")
        else:
            Game.Owon = 1
            Game.puncteO += 1
            rand.config(text = "O WON")
    elif r1_1.text == r2_2.text == r3_3.text:
        Game.winflag = 1
        r1_1.btn.config(bg = color)
        r2_2.btn.config(bg = color)
        r3_3.btn.config(bg = color)
        if r1_1.text == "X":
            Game.Xwon = 1
            Game.puncteX += 1
            rand.config(text = "X WON")
        else:
            Game.Owon = 1
            Game.puncteO += 1
            rand.config(text = "O WON")
    elif r1_3.text == r2_2.text == r3_1.text:
        Game.winflag = 1
        r1_3.btn.config(bg = color)
        r2_2.btn.config(bg = color)
        r3_1.btn.config(bg = color)
        if r1_3.text == "X":
            Game.Xwon = 1
            Game.puncteX += 1
            rand.config(text = "X WON")
        else:
            Game.Owon = 1
            Game.puncteO += 1
            rand.config(text = "O WON")      
    if Game.winflag == 1:
        r1_1.btn.config(state = "disabled")
        r1_2.btn.config(state = "disabled")
        r1_3.btn.config(state = "disabled")
        r2_1.btn.config(state = "disabled")
        r2_2.btn.config(state = "disabled")
        r2_3.btn.config(state = "disabled")
        r3_1.btn.config(state = "disabled")
        r3_2.btn.config(state = "disabled")
        r3_3.btn.config(state = "disabled")
        Game.scor()
        gameover()
    if Game.turn == 9 and Game.winflag == 0:
        Game.tie = 1
        gameover()
        rand.config(text = "TIE")

def about():
    msg = messagebox.showinfo("About", "Created by Alex.")

def newgame():
    global r1_1, r1_2, r1_3, r2_1, r2_2, r2_3, r3_1, r3_2, r3_3
    del r1_1, r1_2, r1_3, r2_1, r2_2, r2_3, r3_1, r3_2, r3_3
    Game.winflag = 0
    Game.turn = 0
    Game.tie = 0
    Game.Xwon = 0
    Game.Owon = 0
    r1_1 = Game(0, 0, "1")
    r1_2 = Game(0, 1, "2")
    r1_3 = Game(0, 2, "3")
    r2_1 = Game(1, 0, "4")
    r2_2 = Game(1, 1, "5")
    r2_3 = Game(1, 2, "6")
    r3_1 = Game(2, 0, "7")
    r3_2 = Game(2, 1, "8")
    r3_3 = Game(2, 2, "9")
    rand.config(text = "Current turn: X")

def gameover():
    if Game.Xwon == 1:
        msg = messagebox.askquestion("Game over!", "X WON!!!\nPlay again?")
    elif Game.Owon == 1:
        msg = messagebox.askquestion("Game over!", "O WON!!!\nPlay again?")
    elif Game.tie == 1:
        msg = messagebox.askquestion("Game over!", "TIE!!!\nPlay again?")
    if msg == "yes":
        newgame()

def leavegame():
    msg = messagebox.askquestion("Quit?", "Are you sure about this?")
    if msg == "yes":
        root.destroy()
        quit()

#main window
root = tk.Tk()
root.resizable(0,0)
root.title("X si O")

#frames
game = tk.Frame(root)
game.pack()

bottom = tk.Frame(root)
rand = tk.Label(bottom, text = "Current turn: X")
rand.grid(row = 3)
scor = tk.Label(bottom, text = f"SCOREBOARD:  X: {Game.puncteX}     O: {Game.puncteO}")
scor.grid(row = 4)
bottom.pack()

#menus
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff = 0)

menubar.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "New game", command = newgame)
filemenu.add_command(label = "Reset score", command = reset)
filemenu.add_separator()
filemenu.add_command(label="Exit", command = leavegame)

menubar.add_command(label="About", command = about)
root.config(menu = menubar)

#buttons
r1_1 = Game(0, 0, "1")
r1_2 = Game(0, 1, "2")
r1_3 = Game(0, 2, "3")
r2_1 = Game(1, 0, "4")
r2_2 = Game(1, 1, "5")
r2_3 = Game(1, 2, "6")
r3_1 = Game(2, 0, "7")
r3_2 = Game(2, 1, "8")
r3_3 = Game(2, 2, "9")

root.mainloop()

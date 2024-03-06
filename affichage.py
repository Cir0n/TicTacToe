from tkinter import *

def clear():
    """
    Efface tous les slaves de la window pour clear la fenêtre
    """
    list = window.grid_slaves()
    for l in list:
        l.destroy()

    list = window.slaves()
    for l in list:
        l.destroy()
    
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_columnconfigure(3, weight=1)





def menu():

    titlelabel = Label(window, text="Menu", font=("Courrier", 48), bg="#515A5A", fg ="#E67E22") 
    titlelabel.grid(row=0, column=2)
    
    playButton = Button(window, text="Jouer",font=("Courrier", 30), bg="#515A5A", fg ="#E67E22", command=drawGrid)
    playButton.grid(row=1, column=2,)

def printWinner():
    global win

    if win is False:
        win = True
        print("Le joueur", currentPlayer, "a gagné le jeu")
        window.destroy()

def switch_player():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = '0'
    else:
        currentPlayer = 'X'

def verification(clicked_row, clicked_col):
     # detecter victoire horizontale
    count = 0
    for i in range(3):
        current_button = button[i][clicked_row]
        if current_button['text'] == currentPlayer:
            count += 1
    if count == 3:
        printWinner()

    # detecter victoire verticale
    count = 0
    for i in range(3):
        current_button = button[clicked_col][i]
        if current_button['text'] == currentPlayer:
            count += 1
    if count == 3:
        printWinner()

    # detecter victoire diagonale
    count = 0
    for i in range(3):
        current_button = button[i][i]
        if current_button['text'] == currentPlayer:
            count += 1
    if count == 3:
        printWinner()

    # detecter victoire diagonale inversee
    count = 0
    for i in range(3):
        current_button = button[2-i][i]
        if current_button['text'] == currentPlayer:
            count += 1
    if count == 3:
        printWinner()

    if win is False:
        count = 0
        for col in range(3):
            for row in range(3):
                current_button = button[col][row]
                if current_button['text'] == 'X' or current_button['text'] == '0':
                    count += 1
        if count == 9:
            print("Match nul")

def onButtonClick(row, column):
    clickedButton = button[column][row]
    if clickedButton['text'] == "":
        clickedButton.config(text=currentPlayer)
    if verification(row, column):
        window.destroy()
    switch_player()

def drawGrid():
    clear()
    frame = Frame(window)
    for column in range(3):
        buttonsInCol = []
        for row in range(3):
            boxButton = Button(frame, height=10, width=20, bg ='#707b7c', command=lambda r=row, c=column:onButtonClick(r,c))
            boxButton.grid(row=row, column=column)
            buttonsInCol.append(boxButton)
        button.append(buttonsInCol)
    frame.pack(expand=1)



    
button = []
currentPlayer="X"
win=False

window = Tk()
#window option
window.title("TicTacToe")
# window.iconbitmap("image/puissance4.ico")
window.geometry("1080x720")
window.minsize(720, 480)
window.maxsize(1080, 720)
window.config(background='#515A5A')
# configuration des colonnes pour les menus
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)
drawGrid()

window.mainloop()
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
    playButton.grid(row=1, column=2)


def drawGrid():
    clear()
    for column in range(3):
        for row in range(3):
            boxButton = Button(window)
            boxButton.grid(row=row, column=column)
    


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
from cgitb import text
from random import * 
from tkinter import *

maFenetre = Tk()
maFenetre.title("Chifoumi")

eR = Entry(maFenetre)
lR = Label(maFenetre,text = "Votre choix : ", font=("Arial",12))
lUser = Label(maFenetre,text = "Entrez votre choix : pierre feuille ou ciseaux")
lBot = Label(maFenetre, text = "Choix du bot : ")
lResult = Label(maFenetre,text = "Résultat : ")

def botSelection(): # Sélection aléatoire de l'ordinateur
    n = randint(1,3)
 # Choix aléatoire entre pierre (1), feuille (2) ou ciseaux (3)
    if n == 1:
        bot = "pierre" # Item pierre
    elif n == 2:
        bot = "papier" # Item papier
    else:
        bot = "ciseaux" # Item ciseaux
    return(bot)
 
def Compute():

    R = eR.get() 
    lUser.configure(text = "votre choix : " + R)
    lUser.configure(fg = "green")
    botSelection()
    b = botSelection()
    if str(R) == b:
        lResult.configure(text = "Egalité")
        lBot.configure(text = "choix du bot : " + b)
        lBot.configure(fg = "red")
    elif str(R) == "pierre" & b == "ciseaux":
        lResult.configure(text = "Gagné")
        lBot.configure(text = "choix du bot : " + b)
        lBot.configure(fg = "green")


#Buttons

bQuit = Button(maFenetre, text = "Quit", command = maFenetre.destroy)
bCalc = Button(maFenetre, text = "Jouer", command = Compute)

lR.grid(column = 1, row = 1)
lUser.grid(column = 1, row = 3, columnspan = 2)
bCalc.grid(column = 1, row = 4)
bQuit.grid(column = 2, row = 4)
eR.grid(column = 2, row = 1)
lBot.grid(column = 1, row = 5, columnspan=2)
lResult.grid(column =1, row = 6, columnspan=3)


mainloop()
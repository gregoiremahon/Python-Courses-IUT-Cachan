from cmath import pi
from tkinter import *
from turtle import left
from math import *




maFenetre = Tk()
maFenetre.title("Calcul de la fréquence de coupure 1er ordre")

eR = Entry(maFenetre)
eC = Entry(maFenetre)
lR = Label(maFenetre,text = "Valeur de R : ", font=("Arial",12))
lC = Label(maFenetre,text = "Valeur de C : ", font=("Arial",12))
lFreq = Label(maFenetre,text = "Fréq. de coupure = ???? ")

def Compute():
    C = eC.get()
    R = eR.get() 
    R, C = float(R), float(C)
    fc = (1/(2*pi*R*C))
    fc = round(fc,2)
    strfc = str(fc)
    if fc>1000000:
        fc = fc/1000000
        fc = round(fc,2)
        newText = "Valeur de fréquence "+str(fc) +"MHz"
    elif fc>1000:
        fc = fc/1000
        fc = round(fc,2)
        newText = "Valeur de fréquence "+str(fc) +"KHz"
    else:
        fc = fc
        fc = round(fc,2)
        newText = "Valeur de fréquence "+str(fc)+"Hz"

    # On arrondit
    lFreq.configure(text = newText)
    lFreq.configure(fg = "green")
    
#Labels




#Entries

eR = Entry(maFenetre)
eC = Entry(maFenetre)

#Buttons

bQuit = Button(maFenetre, text = "Quit", command = maFenetre.destroy)
bCalc = Button(maFenetre, text = "Calculer", command = Compute)

lR.grid(column = 1, row = 1)
lC.grid(column = 1, row = 2)
lFreq.grid(column = 1, row = 3, columnspan = 2)
bCalc.grid(column = 1, row = 4)
bQuit.grid(column = 2, row = 4)
eR.grid(column = 2, row = 1)
eC.grid(column = 2, row = 2)


mainloop()
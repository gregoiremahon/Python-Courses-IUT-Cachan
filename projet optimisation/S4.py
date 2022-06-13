### S3


## PROJET OPTIMISATION MAHON GREGOIRE

from math import *
from os import fchdir
from random import random
from statistics import variance
from tkinter import *

from numpy import true_divide

maFenetre = Tk()
maFenetre.title("Meilleur couple RC")

eF = Entry(maFenetre)
lR = Label(maFenetre,text = "Valeur de R : ", font=("Arial",12))
lC = Label(maFenetre,text = "Valeur de C : ", font=("Arial",12))
lFreq = Label(maFenetre,text = "Fréq. de coupure =  ")


listeE24 = [10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 43, 47, 51, 56, 62, 68, 75, 82, 91]
listeE12 = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82]
listeResisE24 = []
listeCapaE12 = []



lExpoR = range(1,6)
lExpoC = range(-12, -6)

LongueurE24 = len(listeE24)
LongueurE12 = len(listeE12)

print("Len liste E24 :" , LongueurE24)
print("Len liste E12 :" , LongueurE12)


for Exposant in lExpoR:
    for Resis in listeE24:
        ValR = 10**(Exposant) * Resis
        listeResisE24.append(ValR)

for Expo in lExpoC:
    for Capa in listeE24:
        ValC = 10**(Expo) * Capa
        listeCapaE12.append(ValC)  

Rmin = min(listeResisE24)
Rmax = max(listeResisE24)
Cmin = min(listeCapaE12)
Cmax = max(listeCapaE12)


freqDes = 125000




def formuleFreq(resis,capa):
   fc = 1/(2*pi*resis*capa)
   return fc

print("fc = ", formuleFreq(Rmin,Cmax),"Hz")
freq = 15000

Fmax = formuleFreq(Rmin,Cmin)
Fmin = formuleFreq(Rmax,Cmax)
def verifFreq(freq):
    return (float(freq) <= float(Fmax) and float(freq) >= float(Fmin))
    
Verification = verifFreq(freqDes)

print("verif freq", Verification)


def trouveRC(maFreqDes):
    Rbest, Cbest, Rbest2, Cbest2 = 0, 0, 0, 0
    erreur = 1e20
    freqc = maFreqDes
    for Val1 in listeResisE24:
        for Val2 in listeCapaE12:
            freqTemp = 1/(2*pi*Val1*Val2)
            if (abs(maFreqDes-freqTemp) <= erreur):
                erreur = abs(maFreqDes - freqTemp)
                Rbest2 = Rbest
                Cbest2 = Cbest
                Rbest= Val1
                Cbest = Val2
                
                   
    ValuesList = [Rbest, Cbest, Rbest2, Cbest2]
    return ValuesList

print("freqDes = ", freqDes)
print("Couples : ", trouveRC(3400))
print("verif : ", formuleFreq(130000, 3.6e-10))



def Compute():
    frequence = eF.get()
    fc = round(float(frequence), 2)
    CoupleRC = trouveRC(float(frequence))
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
    ValeurR1 = CoupleRC[0]
    ValeurC1 = CoupleRC[1]
    
    # On arrondit
    lFreq.configure(text = newText)
    lFreq.configure(fg = "green")
    lR.configure(text = ValeurR1)
    lC.configure(fg = "green")
    lC.configure(text = ValeurC1)
    lC.configure(fg = "green")
    print(CoupleRC)
    
    return CoupleRC






bQuit = Button(maFenetre, text = "Quit", command = maFenetre.destroy)
bCalc = Button(maFenetre, text = "Calculer", command = Compute)

lR.grid(column = 1, row = 1)
lC.grid(column = 1, row = 2)
lFreq.grid(column = 1, row = 3, columnspan = 2)
bCalc.grid(column = 1, row = 4)
bQuit.grid(column = 2, row = 4)
eF.grid(column = 3, row = 5)


mainloop()



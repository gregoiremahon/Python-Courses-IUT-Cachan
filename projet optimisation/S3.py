### S3


## PROJET OPTIMISATION MAHON GREGOIRE

from math import *
from random import random
from statistics import variance

from numpy import true_divide

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




## PROJET OPTIMISATION MAHON GREGOIRE

from math import *

listeE24 = [10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 43, 47, 51, 56, 62, 68, 75, 82, 91]
listeE12 = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82]
listeResis = []
listeCapa = []


lExpoR = range(1,6)
lExpoC = range(-12, -6)

LongueurE24 = len(listeE24)
LongueurE12 = len(listeE12)

print("Len liste E24 :" , LongueurE24)
print("Len liste E12 :" , LongueurE12)


for Exposant in lExpoR:
    for Resis in listeE24:
        ValR = 10**(Exposant) * Resis
        listeResis.append(ValR)

for Expo in lExpoC:
    for Capa in listeE24:
        ValC = 10**(Expo) * Capa
        listeCapa.append(ValC)  


print("Liste Resistances : ", listeResis)
print("Liste Capa : ", listeCapa)


print("rmax",min(listeResis))
print("rmin", max(listeResis))
print("cmin", min(listeCapa))
print("cmax", max(listeCapa))

## TEST PARTIE 2

prenom = "Grégoire"
NomFamille = "Mahon"
Np = 0
Nn = 0

for Letters in range(len(prenom)):

     Np = Np + 1

for Letters in range(len(NomFamille)):

     Nn = Nn + 1

print("Mon prénom est : ", prenom)
print(Np, ": Longueur de mon prénom")
print("Mon nom de famille est : ", NomFamille)
print(Nn, ": Longueur de mon nom de famille")

## Somme : 

SommeLongueurs = Np + Nn

## Suite de Padovan
def Padovan(SommeLongueurs):
 
   ## Initialisation des premiers termes de la série de Padovan
    nm2, nm1, n, nplus1 = 1, 1, 1, 2
 
    #On cherche la position du terme à la position SommeLongueurs (Np + Nn)
    for i in range(3, SommeLongueurs+1):
        nplus1 = nm2 + nm1
        nm2 = nm1
        nm1 = n
        n = nplus1
 
    return nplus1
 

print("Somme des longueurs de mon prénom et de mon nom (Np + Nn)", SommeLongueurs)
print("Nombre à la position", SommeLongueurs,"dans la suite de Padovan :", Padovan(SommeLongueurs))
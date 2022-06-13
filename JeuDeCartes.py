#Jeu de cartes 
# Pic = S
# Carreau = D
# Trèfle = C
# Coeur = H 

# Carte = "hc" avec h = 1,2,3,4,5,6,7,8,9,10,J"Jack",Q"Queen",K"King"

from random import choice
from tkinter import scrolledtext

 ## J Q K = 10pts
 ## 2 à 9 = leur valeur pts
 ## 1 = 1 ou 11 input(pts)
 ## tir, additionne du score, but : se rapprocher le plus possible de 21 sans le dépasser
 ## Le joueur le plus proche de 21 gagne
 
Score_dict = {"2": 2, "3": 3, "4": 4,"5":5,"6":6,"7":7,"8":8,"9":9,"t":10,"j":10,"q":10,"k":10}





 
hauteurs = [str(valeur) for valeur in range (1,10)] + ["t","j","q","k"] # t = ten = chiffre 10
couleurs = ["s","h","d","c"]
jeuCartes = []

# Construction du jeu de 52 cartes
for couleur in couleurs:
    for hauteur in hauteurs: 
        jeuCartes.append(hauteur+couleur)

mainJ1 = [choice(jeuCartes), choice(jeuCartes)]

def score1carte(laCarte):
    hauteur = laCarte[0]
    if hauteur in "tjqk":
        return 10
    else:
        return int(hauteur)

def compter(laMain): 
    score = 0       
    for cartes in laMain:
        score = score + score1carte(cartes) 
    return score


print(mainJ1)

compter(mainJ1)


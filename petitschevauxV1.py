## Projet guidé POO

#Jeu des petits chevaux POO

from random import *

class cJoueur():
    def __init__(self,nomJoueur):
        self.nomJoueur = nomJoueur
        self.lPos = ['OUT']
    def lancerDe(self):
        lanceJoueur = randrange(1,7)
        return lanceJoueur
        



Joueur1 = cJoueur("Matthieu")
resultatJ1 = Joueur1.lancerDe()
print(Joueur1.nomJoueur,"a obtenu",resultatJ1,"au lancé de dé")
# Jeu du 421

from random import *

class cJoueur(): ## Classe joueur
    def __init__(self,nomJoueur):
        self.nomJoueur = nomJoueur ## Nom du joueur
        self.Valeurs = [] ## Liste des valeurs des lancés de dés

    def LancerLesDes(self):

        for Lancers in range(3):
            Lancers = self.lanceJoueur = randrange(1,7)
            self.Valeurs.append(Lancers)
        return self.Valeurs

Joueur = cJoueur("MAHON")
print(Joueur.LancerLesDes())

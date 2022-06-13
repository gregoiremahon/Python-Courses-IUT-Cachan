# Jeu du 421

from random import *

class cJoueur(): ## Classe joueur
    def __init__(self,nomJoueur):
        self.nomJoueur = nomJoueur ## Nom du joueur
        self.Valeurs = [] ## Liste des valeurs des lancés de dés

    def LancerLesDes(self): # Méthode lancer de 3 dés
        self.Valeurs = [4, 2, 1]
        for Lancers in range(3):  # Lancers des dés 0 1 et 2 (3 dés au total)
            Lancers = self.lanceJoueur = randrange(1,7) # Valeur aléatoire entre 1 et 6 simulant un dé à 6 faces
            self.Valeurs.append(Lancers) # Ajout de la valeur obtenue dans la liste Valeurs
        return self.Valeurs # Renvoie la liste Valeurs
    
    def verifier421(self):
        if (self.Valeurs[0] == 4):
            if (self.Valeurs[1] == 2):
                if (self.Valeurs[2] == 1):
                    return True
                else:
                     return False

Joueur = cJoueur("MAHON")
print(Joueur.LancerLesDes())
print(Joueur.LancerLesDes())
print(Joueur.LancerLesDes())
print(Joueur.LancerLesDes())
print(Joueur.verifier421())
print(Joueur.verifier421())
print(Joueur.verifier421())
print(Joueur.verifier421())
print(Joueur.verifier421())
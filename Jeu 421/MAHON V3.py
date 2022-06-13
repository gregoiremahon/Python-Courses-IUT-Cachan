# Jeu du 421

from random import *

class cJoueur(): ## Classe joueur
    def __init__(self,nomJoueur):
        self.nomJoueur = nomJoueur ## Nom du joueur
        self.Valeurs1 = [] ## Liste des valeurs des lancés de dés

    def LancerLesDes(self): # Méthode lancer de 3 dés
        self.Valeurs = []
        for Lancers in range(3):  # Lancers des dés 0 1 et 2 (3 dés au total)
            Lancers = self.lanceJoueur = randrange(1,7) # Valeur aléatoire entre 1 et 6 simulant un dé à 6 faces
            self.Valeurs.append(Lancers) # Ajout de la valeur obtenue dans la liste Valeurs
        return self.Valeurs # Renvoie la liste Valeurs
    
    def verifier421(self):
        if (self.Valeurs[0] == 4): # Si le premier élement de la liste (premier dé) vaut 4 alors continuer la vérif
            if (self.Valeurs[1] == 2): # Si le second élement de la liste vaut 2 alors continuer la vérif
                if (self.Valeurs[2] == 1): # Si le troisième élément de la liste vaut 1, alors on a 421
                    return True # Dans le cas où un des lancers donne 421, alors la méthode renvoie True
                else:
                     return False # Si on a pas de 421, alors la méthode renvoie False
    
    def verifierBaraque(self):
        if self.Valeurs[0] == self.Valeurs[1]: 
            if self.Valeurs[1]==self.Valeurs[2]:
                return True
            else:
                return False


Joueur = cJoueur("MAHON")
print(Joueur.LancerLesDes())
print(Joueur.LancerLesDes())
print(Joueur.LancerLesDes())
print(Joueur.LancerLesDes())
print("Vérification 421 donne :", Joueur.verifier421())
print("Vérification 421 donne :", Joueur.verifier421())
print("Vérification 421 donne :", Joueur.verifier421())
print("Vérification 421 donne :", Joueur.verifier421())
print("Vérification 421 donne :", Joueur.verifier421())
print("Vérification Baraque donne :", Joueur.verifierBaraque())
print("Vérification Baraque donne :", Joueur.verifierBaraque())
print("Vérification Baraque donne :", Joueur.verifierBaraque())
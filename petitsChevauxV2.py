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
        
class cPetitsChevaux():
    
    def __init__(self):
        self.nbTours = 1
        self.listeJoueurs = []

    def ajouterJoueur(self):
        nomJoueur = input('Quel est le nom du joueur ?')
        self.listeJoueurs.append(nomJoueur)
        print("Liste des joueurs actualisée :", self.listeJoueurs)
        print("Nombre de joueurs :", len(self.listeJoueurs))
    def demarrerPartie(self):
        pass
    def demarrerTour(self):
        pass



Joueur1 = cJoueur("Matthieu")
resultatJ1 = Joueur1.lancerDe()
print(Joueur1.nomJoueur,"a obtenu",resultatJ1,"au lancé de dé")

jeu = cPetitsChevaux()
jeu.ajouterJoueur()
jeu.ajouterJoueur()
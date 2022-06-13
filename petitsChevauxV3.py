## Projet guidé POO

#Jeu des petits chevaux POO

from random import *
from copy import *
from xml.dom import NOT_FOUND_ERR

class cJoueur():
    def __init__(self,nomJoueur):
        self.nomJoueur = nomJoueur
        self.lPos = ['OUT']
    def lancerDe(self):
        self.lanceJoueur = randrange(1,7)
        return self.lanceJoueur
        
class cPetitsChevaux():
    
    def __init__(self):
        self.nbTours = 1
        self.listeJoueurs = []
        self.nTour = 0

    def ajouterJoueur(self):
        nomJoueur = input('Quel est le nom du joueur ?')
        self.listeJoueurs.append(nomJoueur)
        print("Liste des joueurs actualisée :", self.listeJoueurs)
        print("Nombre de joueurs :", len(self.listeJoueurs))

    def demarrerPartie(self):
        if len(self.listeJoueurs)>0:
            self.demarrerTour()
        else:
            print("No player")

    def demarrerTour(self):
        self.nTour = self.nTour + 1
        print("Début du tour",self.nTour)
        for chaqueJoueur in self.listeJoueurs:
            ScoreJoueur = cJoueur(chaqueJoueur).lancerDe()
            print("Au tour de",cJoueur(chaqueJoueur).nomJoueur,", il a obtenu",ScoreJoueur,"au lancé de dé")
            if ScoreJoueur == 6:
                print("Bien, le joueur", cJoueur(chaqueJoueur).nomJoueur,"fait sortir son cheval de l'écurie")
                cJoueur(chaqueJoueur).lPos = [0]
                print("votre cheval est en position",cJoueur(chaqueJoueur).lPos)
            else:
                print("Aucun joueur n'a obtenu 6 au lancé de dé, les chevaux restent dans l'écurie")

jeu = cPetitsChevaux()
jeu.ajouterJoueur()
jeu.ajouterJoueur()
jeu.ajouterJoueur()
jeu.demarrerPartie()


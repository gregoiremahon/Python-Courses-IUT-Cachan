## Code mardi 7 juin AM
## POO


from math import *

class cPromo():
    def __init__(self,nom):
        self.nomPromo = nom
        self.listeEtudiants = []
    
    def ajouterEtudiant(self,etudiant):
        self.listeEtudiants.append(etudiant)
        print('Nouvel effectif de la promo:', len(self.listeEtudiants))
    
    def listerLesEtudiants(self):
        cpt = 1
        for self.etudiant in self.listeEtudiants:
            print(cpt,'',self.etudiant.nom,self.etudiant.prenom)
            cpt += 1

class cEtudiant():

    def __init__(self,nom,prenom,age): ##Constructeur init
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.listeNotes = []

    def ajouterNote(self):
        laNote = float(input('Quelle note ajouter ? '))
        self.listeNotes.append(laNote)
        print('Notes modifiées pour',self.nom,'->',self.nom,'',self.prenom,' -> ',self.listeNotes)

    def calculerMoyenne(self):
        Total = 0
        if len(self.listeNotes) == 0:
            print('Pas de notes, pas de moyenne')
        else:
            Somme = sum(self.listeNotes)
            nbNotes = len(self.listeNotes)
            Moyenne = Somme/nbNotes
        print("La moyenne des notes de ", self.nom, self.prenom,"est", Moyenne)


        
maPromo = cPromo("APP2 21/22")

etu1 = cEtudiant("Elgoyhen","Matthieu",21)
etu2 = cEtudiant("Pouth-Bichot", "Andreas",20)

maPromo.ajouterEtudiant(etu1)
maPromo.ajouterEtudiant(etu2)
maPromo.listerLesEtudiants()
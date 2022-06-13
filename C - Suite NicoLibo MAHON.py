# Suite de Fibonnacci



prenom = 'gregoire'
nom = 'mahon'
longueurNom = len(nom)
Nn = longueurNom
LongueurPrenom = len(prenom)
Np = LongueurPrenom
Np2= LongueurPrenom **2

print("Np * Nn = ", Np*Nn)

def NicoLibo():
    
    n0 = 1.5
    n1 = 1.5
 
    print("\n la suite NicoLibo est :")
    print(n0)
    print(n1)
    
    cptSuite = 3

    while(cptSuite < Np * Nn):
        
        n2 = n1 + n0
        n3 = n2 + n0
        cptSuite +=1
        rapport = n2 / n1
        print("Compteur = ",cptSuite, "Valeur = ", n3)
        #print("Rapport des 2 derniers nombres = ", rapport)


NicoLibo()

from logging import shutdown
from random import randrange

Value = randrange(4)
Tentatives = 3

while(Tentatives <=3):

    Test1 = int(input("Trouvez le nombre: "))
    if (Test1 > Value):
        print("Valeur trop grande")
    elif (Test1 < Value):
        print("Valeur trop petite")
    else:
        print("Bien joué, vous avez trouvé la valeur : ", Value)
        break
    Tentatives += 1
    

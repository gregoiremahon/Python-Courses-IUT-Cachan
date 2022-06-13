# Cours Python N.Liebeaux 10 mai 2022
# Exercice cryptographie de base 
# CODAGE DE JULES CESAR
# Pour chaque lettre du mot original, on décale chaque lettre de 10 lettres dans l'alphabet

from cgi import test


alphabet = "abcdefghijklmnopqrstuvwxyz"

decalage = int(input("Quelle valeur de décalage ? "))
mot = input("Quel mot à coder ? ")

def cryptage(mot):
    MessageCode = ""
    for letters in range(len(mot)):
        lettre = mot[letters]
        PosAlphabet = alphabet.index(lettre)
        posCodee = (PosAlphabet + decalage) % len(alphabet)
        NewLetter = alphabet[posCodee]
        MessageCode = MessageCode + NewLetter
    print("mot à coder : ",mot)
    return MessageCode
    #print("Message codé : ",MessageCode)

MotCrypte = cryptage(mot)
print("Mot crypté", MotCrypte)


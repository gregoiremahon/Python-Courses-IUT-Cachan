## Test Partie 2 question 3

leMot = "test" # A définir
Score1pt = ["E", "A", "I", "N", "O", "R", "S", "T", "U", "L"]
Score2pt = ["D", "M", "G"]
Score3pt = ["B", "C", "P"]
Score4pt = ["F", "H", "V"]
Score8pt = ["J", "Q"]
Score10pt = ["K", "W", "X", "Y", "Z"]


def Scrabble(leMot):
    Score = 0
    cpt = 0
    for Letters in leMot:
        Position = leMot[cpt]
        print(leMot[cpt])
        if Position in Score1pt:
            Score = Score + 1
        if Position in Score2pt:
            Score = Score + 2
        if Position in Score3pt:
            Score = Score +3
        if Position in Score4pt:
            Score = Score + 4
        if Position in Score8pt:
            Score = Score + 8 
        if Position in Score10pt:
            Score = Score + 10
        cpt = cpt+1
    return Score
        
print("Score de votre mot : ", Scrabble(str(input("Votre ville en majuscule ?"))))


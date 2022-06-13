# Prog 10 juin

# BlockChain

#Encoding

from hashlib import *
from datetime import *
from sqlite3 import Timestamp
from urllib.request import CacheFTPHandler
class Bloc():
    def __init__(self,data):
        self.idBloc = 0
        self.data = data
        self.nonce = 0
        self.Hash = ""
        self.PrevHash = ""
        self.datetime = 0
        self.instant = 0

    def afficherBloc(self):
        print('id Bloc :', self.idBloc)
        #data = input('Quelle data pour ce bloc ?')
        print('data :', self.data)
        self.PrevHash = self.Hash
        self.Hash= sha256(self.data.encode('UTF-8'))
        print('Prev Hash :', self.PrevHash)
        print('Hash :', self.Hash.hexdigest())
        print("date : ", self.datetime)
    
    def CalculerHash(self):
        empreinte = sha256()
        empreinte.update(str(self.idBloc).encode('UTF-8'))
        empreinte.update(self.data.encode('UTF-8'))
        empreinte.update(str(self.datetime).encode('UTF-8'))
        empreinte.update(self.Hash.encode("UTF-8"))
        
        return empreinte.hexdigest()

class meteoChain():
    def __init__(self):
        self.blockChain = []
        

    def initierChaine(self):
        blocGenesis = Bloc("")
        blocGenesis.datetime = datetime.now()
        HashBlocGenesis = blocGenesis.CalculerHash()
        self.blockChain.append(blocGenesis)
    
    def afficherChaine(self):
        for bloc in self.blockChain:
            Bloc.afficherBloc(bloc)

    def ajouterBloc(self):
        newBloc = Bloc(input('Quelle est la température ?'))
        newBloc.
        self.blockChain.append(newBloc)
    
    def afficherLongueurChaine(self):
        Length = len(self.blockChain)
        print('Nombre de blocs : ', Length)



maBlockChain = meteoChain()
maBlockChain.initierChaine()
maBlockChain.afficherChaine()
maBlockChain.ajouterBloc()
maBlockChain.ajouterBloc()
maBlockChain.ajouterBloc()
maBlockChain.ajouterBloc()
maBlockChain.afficherLongueurChaine()


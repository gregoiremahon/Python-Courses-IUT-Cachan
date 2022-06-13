# Heritage

from platform import python_branch

from cv2 import CALIB_CB_NORMALIZE_IMAGE


class cAnimal():
    def __init__(self,nomCommun,espece):
        self.nomCommun = nomCommun
        self.espece = espece

    def presenter(self):
        print('Bonjour, je suis un', self.nomCommun)

class cTigre(cAnimal):
    def __init__(self,nomCommun,espece,):
        cAnimal.__init__(self,nomCommun,espece)
        self.habitat = "Bengale"

python = cAnimal("Python", 'serpent')
python.presenter()
sherekhan = cTigre('Tigre','Felins')
print(sherekhan)
print(sherekhan.espece,sherekhan.habitat)
sherekhan.presenter() ## Heritage, on utilise la fonction présenter de la classe mère
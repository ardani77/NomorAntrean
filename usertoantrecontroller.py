from account import Account
from antre import Antre
from antreansekarang import AntreanSekarang

class User_Look:
    def __init__(self):
        self.account = Account()
        self.antre = Antre()
        self.antreansekarang = AntreanSekarang()

    def showAntreanTersedia(self):
        return self.antreansekarang.showTersedia()

    def getNomorAntrean(self):
        return self.antre.getAntre()

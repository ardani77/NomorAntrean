from account import Account
from antre import Antre
from antreansekarang import AntreanSekarang

class User_Controller:
    def __init__(self, username):
        self.account = Account(username)
        self.antre = Antre()
        self.antreansekarang = AntreanSekarang()

    def getName(self):
        return self.account.getname()

    def getNomor(self):
        return self.antre.getAntre()

    def showNomor_Tersedia(self):
        return str(self.antreansekarang.showTersedia())

    def showNomor_Antrean(self):
        return self.antre.showAntre()

##if __name__ == "__main__":
##    tes = User_Controller("budi123")
##    print(tes.getName())
##    print(tes.getNomor())
##    print(tes.showNomor_Tersedia())
##    print(tes.showNomor_Antrean())

    


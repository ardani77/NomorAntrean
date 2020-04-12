import Account
import AntreanSekarang

class Admin_Antre:
    def __init__(self):
        self.account = Account()
        self.antreansekarang = AntreanSekarang()

    def tambahAntrean(self):
        return self.antreansekarang.tambahnomor()

    def kurangiAntrean(self):
        return self.antreansekarang.kurangnomor()

    def resetAntrean(self):
        return self.antreansekarang.reset

    def showAntrean(self):
        return self.antreansekarang.showTersedia()

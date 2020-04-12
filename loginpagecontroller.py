from account import Account

class LoginController:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def checkTruth(self):
        a = Account(self.username)
        password = a.getpassword()
        if self.password == password:
            return True
        return False

    def checkRole(self):
        a = Account(self.username)
        return a.getrole()

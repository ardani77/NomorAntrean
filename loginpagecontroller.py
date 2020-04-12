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

##if __name__ == "__main__":
##    tes = LoginController("budi123", "00000")
##    print(tes.checkTruth())
##    print(tes.checkRole())
##    if tes.checkRole() == "User":
##        print("True")
##    else:
##        print("FALSE")

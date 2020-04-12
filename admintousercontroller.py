import Account

class Admin_User:
    def __init__(self):
        self.account = Account()

    def showAllUser(self):
        alluser = []
        user = self.account.showUser()
        for i in user:
            alluser.append(i)
        return alluser

    def addUser(self, name, username, password):
        role = 'user'
        return self.account.add(name, username, password)

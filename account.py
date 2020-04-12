import pymongo

class Account:

    def __init__(self,username = None):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["nomorantrean"]
        self.collect_account = db["account"]
        if username:
            self.username = username

    def getlistname(self):
        listname = []
        for accountname in self.collect_account.find():
            listname.append(accountname["name"])
        return listname

    def add(self,username,password,name,role):
        dictaccount = {"username":username,"password":password,"name":name,"role":role}
        return self.collect_account.insert_one(dictaccount)

    def getdata(self):
        return self.collect_account.find_one({'username':self.username})

    def getname(self):
        get = self.collect_account.find_one({'username':self.username})
        if get == None:
            return None
        return get['name']

    def setname(self,newname):
        query = {"username": self.username}
        set = {"$set":{"name":newname}}
        return self.collect_account.update_one(query,set)

    def getpassword(self):
        get = self.collect_account.find_one({'username':self.username})
        if get == None:
            return None
        return get['password']

    def setpassword(self, newpassword):
        query = {"username": self.username}
        set = {"$set": {"password": newpassword}}
        return self.collect_account.update_one(query, set)

    def getusername(self):
        return self.username

    def getrole(self):
        get = self.collect_account.find_one({'username':self.username}, {"role" : 1})
        if get == None:
            return None
        return get['role']

    def setrole(self,newrole):
        query = {"username": self.username}
        set = {"$set":{"role":newrole}}
        return self.collect_account.update_one(query,set)

    def showUser(self):
        x = []
        if x == None:
            return None
        for i in self.collect_username.find():
            x.append(i)
        return x



##input = input("masukan username: ")
##account = Account(input)
##print(account.getname())
##print(account.getusername())
##print(account.getpassword())
##print(account.getrole())
##for name in account.getlistname():
##    print(name)

import pymongo
from bson.objectid import ObjectId

class Antre:

    def __init__(self, id = None):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["nomorantrean"]
        self.collect_antre = db["antre"]
        self.collect_antreansekarang = db["antreansekarang"]
        if id:
            self.id = ObjectId(id)

    def getData(self):
        return self.collect_antre.find_one({"_id":self.antre})
    
    def getAntre(self):
        ambilnomor = self.collect_antreansekarang.find({},{"_id" : 0})
        if ambilnomor == None:
            return None
        x = []
        for i in ambilnomor:
            x.append(i)
        self.collect_antre.insert_many(x)
        nomor = self.collect_antreansekarang.find_one()
        nomorantrean = int((nomor['antrean']))
        update = {"$set": { "antrean" : nomorantrean + 1 }}
        self.collect_antreansekarang.update_one(nomor, update)
        return x

    def showAntre(self):
        x = []
        if x == None:
            return None
        for i in self.collect_antre.find({},{"_id" : 0}):
            x.append(i)
        return x
       




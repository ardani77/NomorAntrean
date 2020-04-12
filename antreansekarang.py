import pymongo

class AntreanSekarang:

    def __init__(self, antreansekarang = None):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["nomorantrean"]
        self.collect_antreansekarang = db["antreansekarang"]
        if antreansekarang:
            self.antreansekarang = ObjectId(id)

    def tambahnomor(self):
        nomor = self.collect_antreansekarang.find_one()
        nomorantrean = int((nomor['antrean']))
##        nomorid = int((nomor['_id']))
        update = {"$set": { "antrean" : nomorantrean + 1 }}
##        updateid = {"$set": { "_id" : nomorid + 1 }}
        return self.collect_antreansekarang.update_one(nomor, update)

    def kurangnomor(self):
        nomor = self.collect_antreansekarang.find_one()
        nomorantrean = int((nomor['antrean']))
        update = {"$set": { "antrean" : nomorantrean - 1 }}
        return self.collect_antreansekarang.update_one(nomor, update)

    def resetnomor(self):
        nomor = self.collect_antreansekarang.find_one()
        nomorantrean = int((nomor['antrean']))
        if nomorantrean > 1:
            nomorantrean = 1
        else:
            nomorantrean = 1
        update = {"$set": { "antrean" : nomorantrean}}
        return self.collect_antreansekarang.update_one(nomor, update)

    def showTersedia(self):
        x = []
        if x == None:
            return None
        for i in self.collect_antreansekarang.find():
            x.append(i)
        return x


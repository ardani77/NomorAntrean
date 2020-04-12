import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["nomorantrean"]
collect_account = db["account"]
collect_antre = db["antre"]
collect_antreansekarang = db["antreansekarang"]

accountdict = [
    {"_id" : "0", "username":"ardani123","password":"00000","name":"Muhammad Ardani","role":"Administrator"},
    {"_id" : "1", "username":"budi123","password":"00000","name":"Budi","role":"User"},
    {"_id" : "2", "username":"andi123","password":"00000","name":"Andi","role":"User"},
    {"_id" : "3", "username":"padi123","password":"00000","name":"Padi","role":"User"},
    {"_id" : "4", "username":"dedi123","password":"00000","name":"Dedi","role":"User"},
    {"_id" : "5", "username":"kadi123","password":"00000","name":"Kadi","role":"User"},
    {"_id" : "6", "username":"rudi123","password":"00000","name":"Rudi","role":"User"},
]

antredict = [
    {"_id" : "1"}
]

antreansekarangdict = [
    {"_id" : "1", "antrean" : "1"}

]

a = collect_account.insert_many(accountdict)
b = collect_antre.insert_many(antredict)
c = collect_antreansekarang.insert_many(antreansekarangdict)
print(client.list_database_names())
##
print(db.list_collection_names())
##
print(a.inserted_ids)
print(b.inserted_ids)
print(c.inserted_ids)

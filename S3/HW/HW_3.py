import json
from pprint import pprint

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client["books"]
info = db.info

info.delete_many({})

with open("data.json", "r", encoding="UTF-8") as f:
    books = json.load(f)

for book in books:
    info.insert_one(book)

#   книги с ценой выше 57
for doc in info.find({"price": {"$gt": 57}}):
    pprint(doc)

#   книги где в описании есть слово vacation
for doc in info.find({"description": {"$regex": "[Vv]acation"}}):
    pprint(doc)

#   книги у которых цена от 35 до 40 и в наличии от 5 до 10
for doc in info.find({"price": {"$gt": 35.0, "$lt": 40.0},
                      "available": {"$gt": 5, "$lt": 10}}):
    pprint(doc)

#   книги где в описании есть слово France или цена от от 35 до 40
for doc in info.find({"$or": [{'description': {"$regex": "France"}}, {"price": {"$gt": 35.0, "$lt": 40.0}}]}):
    pprint(doc)

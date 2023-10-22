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


for doc in info.find({"price": {"$gt": 57}}):
    pprint(doc)

for doc in info.find({"description": {"$regex": "[Vv]acation"}}):
    pprint(doc)

for doc in info.find({"price": {"$gt": 35.0, "$lt": 40.0},
                      "available": {"$gt": 5, "$lt": 10}}):
    pprint(doc)


for doc in info.find({"$or": [{'description': {"$regex": "France"}}, {"price": {"$gt": 35.0, "$lt": 40.0}}]}):
    pprint(doc)

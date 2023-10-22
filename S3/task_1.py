from pprint import pprint
from pymongo.errors import *

from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client["users"]
# db2 = client["books"]

persons = db.persons

# doc = {"_id": "fcf3wafw4a2raerg4w3",      # если не указать, то подставит рандомный
#        "author": "Peter",
#        "age": 38,
#        "text": "is cool!",
#        "tags": ["cool", "hot", "ice"],
#        "date": "14.06.1983"}
#
# try:
#     persons.insert_one(doc)
# except DuplicateKeyError as e:
#     print(e)

authors_list = [
    {"author": "John",
     "age": 38,
     "text": "is cool!",
     "tags": ["cool", "hot", "ice"],
     "date": "14.06.1983"},
    {"author": "Peter",
     "age": 44,
     "text": "Hot cool!!!",
     "title": "easy too!",
     "date": "30.05.1997"},
    {"author": "Anna",
     "age": 31,
     "text": "Nice book!!!",
     "tags": ["fantastic", "criminal"],
     "date": "14.06.1983"}]

# persons.insert_many(authors_list)     #   при многократном вызове добовляет тоже содержимое с новыми id

# for doc in persons.find({"age": {"$gt": 40}}):    # поиск возраста больше чем 40
#     pprint(doc)

# for doc in persons.find({"$or": [{'author': "Peter"}, {"age": 31}]}):     # автор Пётр или возраст = 31
#     pprint(doc)


# for doc in persons.find({'author': {"$regex": "J"}}):       # поиск через регулярные выражение
#     pprint(doc)

# persons.update_one({"author": "Peter"}, {"$set": {"author": "Пётр"}})


new_doc = {"author": "Andrey",
           "age": 49,
           "text": "is hottttt!!!!",
           "date": "24.04.1991"}

# persons.update_one({"author": "Peter"}, {"$set": new_doc})
persons.replace_one({"author": "Peter"}, new_doc)

for doc in persons.find():
    pprint(doc)

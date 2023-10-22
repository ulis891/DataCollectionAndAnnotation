import json
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client["crashes"]
info = db.info

info.delete_many({})

with open("crash-data.json", "r", encoding="UTF-8") as f:
    data = json.load(f)

count_duplicated = 0

for feature in data["features"]:
    _id = feature.get("properties").get("tamainid")
    feature["_id"] = _id
    try:
        info.insert_one(feature)
    except:
        count_duplicated += 1
        print(feature)

#
# for doc in info.find({"properties.lat2": {"$gt": 35.0, "$lt": 36.0},
#                       "properties.lon2": {"$gt": -78.0, "$lt": -77.0}}):
#     print(doc)
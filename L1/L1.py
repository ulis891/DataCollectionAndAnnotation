import requests
import json

url = "https://openlibrary.org/search.json"

subject = "Artifical intelligence"

params = {
    "subject" : subject,
    "limit" : 1
}

response = requests.get(url, params=params)

if response.status_code == 200:
    print("Sucess")
else:
    print(f"Faule cod {response.status_code}")

data = json.loads(response.text)

# print(data)

books = data["docs"]

for book in books:
    print("Title: ", book["title"])
    print("Author: ", book["author_name"])
    print("Subject: ", book["subject"])
    print("\n")
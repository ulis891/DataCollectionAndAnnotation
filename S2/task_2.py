from pprint import pprint
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = "https://www.gb.ru"

ua = UserAgent()
haaders = {"UserAgent": ua.chrome}
params = {"page": 1}

session = requests.session()  # что бы маскировать запрос под обычную сессию из браузера

all_posts = []

while True:
    response = session.get(url + "/posts", params=params, headers=haaders)
    soup = BeautifulSoup(response.text, "html.parser")
    posts = soup.find_all("div", {"class": "post-item"})
    if not posts:
        break
    for post in posts:
        post_info = {}
        name_info = post.find("a", {"class": "post-item__title"})
        post_info["name"] = name_info.getText()
        post_info["url"] = url + name_info.get("href")

        add_info = post.find("div", {"class": "text-muted"}).findChildren("span")
        post_info["views"] = int(add_info[0].getText())
        post_info["comments"] = int(add_info[1].getText())

        all_posts.append(post_info)
    print(params["page"])
    params["page"] += 1

pprint(all_posts)
print(len(all_posts))

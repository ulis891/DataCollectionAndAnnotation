"""
Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/
и извлечь информацию о всех книгах на сайте во всех категориях:
название, цену, количество товара в наличии (In stock (19 available)) в формате integer, описание.
"""

from pprint import pprint
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent



page = 1
url = "http://books.toscrape.com/"

ua = UserAgent()
haaders = {"UserAgent": ua.chrome}


session = requests.session()  # что бы маскировать запрос под обычную сессию из браузера

all_books = []
# + "/catalogue/page-1"
response = session.get(url, headers=haaders)
soup = BeautifulSoup(response.text, "html.parser")

posts = soup.find_all("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})

for post in posts:
    book_info = {}
    title = post.find("h3").find("a").get("title")
    book_info["title"] = title
    book_url = url + post.find("h3").find("a").get("href")
    book_info["url"] = book_url
    book_response = session.get(book_url, headers=haaders)
    book_soup = BeautifulSoup(book_response.text, "html.parser")
    available = int(book_soup.find("p", {"class": "instock availability"}).getText().strip().replace("\n", "").split("(")[1].replace(" available)", ""))
    book_info["available"] = available
    pprint(book_info, sort_dicts=False)
    break
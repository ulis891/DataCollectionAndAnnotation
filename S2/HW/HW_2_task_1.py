"""
Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/
и извлечь информацию о всех книгах на сайте во всех категориях:
название, цену, количество товара в наличии (In stock (19 available)) в формате integer, описание.
"""

from pprint import pprint
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json


url = "http://books.toscrape.com/"
ua = UserAgent()
headers = {"UserAgent": ua.random}
session = requests.session()  # что бы маскировать запрос под обычную сессию из браузера
page = 1
all_books = []

while True:
    cat = f"catalogue/page-{page}.html"
    response = session.get(url + cat, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    posts = soup.find_all("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})

    for post in posts:
        book_info = {}

        #   извлекаем название
        title = post.find("h3").find("a").get("title")
        book_info["title"] = title

        #   извлекаем ссылку
        book_url = url + "/catalogue/" + post.find("h3").find("a").get("href")
        book_info["url"] = book_url

        #   извлекаем цену
        book_price = post.find("p", {"class": "price_color"}).getText()
        for leter in book_price:
            if leter.isdigit():
                i = book_price.index(leter)
                break
        book_info["price"] = float(book_price[i:])

        #   извлекаем книгу
        book_response = session.get(book_url, headers=headers)
        book_soup = BeautifulSoup(book_response.text, "html.parser")

        #   извлекаем описание
        try:
            description = book_soup.find("p", attrs=None).getText()
            book_info["description"] = description
        except:
            book_info["description"] = None

        #   извлекаем остаток книг
        available = int(
            book_soup.find("p", {"class": "instock availability"}).getText()
            .strip().replace("\n", "")
            .split("(")[1].replace(" available)", ""))
        book_info["available"] = available

        all_books.append(book_info)

    try:
        print(f'Обработанна страница {page}')
        page += 1
        soup.find("li", {"class": "next"}).find("a").get("href")

    except:
        break

with open('data.json', 'w') as file:
    json.dump(all_books, file)

"""
Написать приложение, которое собирает основные новости с сайта news.mail.ru Для парсинга использовать XPath.
Структура данных должна содержать:
* название источника;
* наименование новости;
* ссылку на новость;
* дата публикации.

Сохраните извлеченные данные в CSV-файл с помощью модуля csv.

Ваш код должен включать следующее:

Строку агента пользователя в заголовке HTTP-запроса, чтобы имитировать веб-браузер и избежать блокировки сервером.
Выражения XPath для выбора элементов данных и извлечения их содержимого.
Обработка ошибок для случаев, когда данные не имеют ожидаемого формата.
Комментарии для объяснения цели и логики кода.
"""

import csv
import os
from pprint import pprint
import requests
from fake_useragent import UserAgent
from lxml import html


url = "https://news.mail.ru/"
ua = UserAgent()
header = {"UserAgent": ua.chrome}
session = requests.session()    # что бы маскировать запрос под обычную сессию из браузера
response = session.get(url, headers=header)
dom = html.fromstring(response.text)

#   добываем все ссылки на новости и чистим их от дубликатов
news_links = list(dict.fromkeys(dom.xpath("//body/div[5]/div[2]/div[1]/div[2]/div[1]/div[1]//a/@href")))

#   создаём список для всех новостей
all_news = []

#   проходимся по всем ссылкам
for item in news_links:
    #   создаем словарь для каждой новости
    news_info_dict = dict()
    #   создаем новый запрос для новостной ссылки
    url = item
    response = requests.get(url, headers=header)
    news = html.fromstring(response.text)
    #   достаём заголовок
    news_info_dict['title'] = news.xpath("//h1/text()")[0]

    #   достаём информацию о дате публикации и источнке
    news_info = news.xpath("//span[@class='note']")
    if news_info:
        news_info_dict['data'] = news_info[0].xpath("//span/@datetime")[0].split('T')[0]
        news_info_dict['sorce'] = news_info[1].xpath("//span[@class='note']//span/text()")[2]
    else:
        #   если нет источника
        news_info_dict['data'] = news.xpath("//span//@datetime")[0].split('T')[0]
        news_info_dict['sorce'] = None
    #   добавляем ссылку
    news_info_dict['url'] = url
    #   добавляем все данные в список
    all_news.append(news_info_dict)

# pprint(all_news, sort_dicts=False)

#   заролняем информацию по заголовкам csv файла
fieldnames = ["title", "data", "sorce", "url"]
#   записываем информацию в файл
with open(os.getcwd() + "/news.csv", "w", encoding="UTF-8", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, dialect="excel", fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_news)

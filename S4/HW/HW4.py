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

from pprint import pprint
import requests
from fake_useragent import UserAgent
from lxml import html

url = "https://news.mail.ru/"
ua = UserAgent()
header = {"UserAgent": ua.chrome}
session = requests.session()  # что бы маскировать запрос под обычную сессию из браузера

response = requests.get(url, headers=header)
dom = html.fromstring(response.text)

news_links = set(dom.xpath("//body/div[5]/div[2]/div[1]/div[2]/div[1]/div[1]//a/@href"))

print(len(news_links))

all_news = []

for item in news_links:
    url = item
    response = requests.get(url, headers=header)
    news = html.fromstring(response.text)
    # news = dom.xpath("//div[@class='article js-article js-module']")
    # date = news.xpath("//span/@datetime")
    news_info = news.xpath("//span[@class='note']")
    pprint(len(news_info))
    data = news_info[0].xpath("//span/@datetime")
    sorce = news_info[1].xpath("//span[@class='note']/a/span/text()")

    print(data, sorce)
    # for note in news_info:
    #     date = note.xpath("//span/@datetime")
    #     sorce = note.xpath("//span[@class='note']/a/span/text()")
    #     print(date, sorce)

    # date = news.xpath("//div[@class='article js-article js-module']//span/@datetime")
    # source = news.xpath("//div[@class='article js-article js-module']//span/@datetime")

    # pprint(date)
    break

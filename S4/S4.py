from pprint import pprint

from lxml import html
import requests
from fake_useragent import UserAgent as ua

header = {ua.chrome}
url = 'https://www.ebay.com'
response = requests.get(url + '/b/Fishing-Equipment-Supplies/1492/bn_1851047', headers=header)
dom = html.fromstring(response.text)

items_list = []
items = dom.xpath("//ul[@class='b-list__items_nofooter']/li")
for item in items:
    item_info = {}

    name = item.xpath(".//h3[@class='s-item__title']/text()")
    link = item.xpath(".//h3[@class='s-item__title']/../@href")
    price = item.xpath(".//span[@class='s-item__price']//text()")
    add_info = item.xpath(".//span[@class='NEGATIVE']/text()")

    item_info['name'] = name
    item_info['link'] = link
    item_info['price'] = price
    item_info['add_info'] = add_info
    items_list.append(item_info)

pprint(items_list)


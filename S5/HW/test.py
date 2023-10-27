from pprint import pprint

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
page = 1
# &page={page}

page_url = f"https://www.litres.ru/search/?q=программирование&languages=ru&art_types=text_book"
url = "https://www.litres.ru"
ua = UserAgent()
haaders = {"UserAgent": ua.chrome}
params = {"ref_": "bo_nb_hm_tab"}

session = requests.session()    #   что бы маскировать запрос под обычную сессию из браузера

response = session.get(page_url, params=params, headers=haaders)

code = response.text

pprint(code)

# soup = BeautifulSoup(response.text, "html.parser")
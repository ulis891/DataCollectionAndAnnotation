from pprint import pprint
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url_full = "https://www.boxofficemojo.com/intl/?ref_=bo_nb_hm_tab"
url = "https://www.boxofficemojo.com"
ua = UserAgent()
haaders = {"UserAgent": ua.random}
params = {"ref_": "bo_nb_hm_tab"}

session = requests.session()    #   что бы маскировать запрос под обычную сессию из браузера

response = session.get(url + "/intl", params=params, headers=haaders)


soup = BeautifulSoup(response.text, "html.parser")

film = {}
films = []

rows = soup.find_all('tr')

for row in rows[2:-1]:
    film = {}

    #   первый способ
    # area_info = row.find('td', {'class': 'mojo-field-type-area_id'}).find('a')
    # film["area"] = [area_info.getText(), url + area_info.get('href')]

    #   второй способ (быстрее работает)
    try:
        area_info = row.find('td', {'class': 'mojo-field-type-area_id'}).findChildren()[0]
        film["area"] = [area_info.getText(), url + area_info.get('href')]
    except:
        continue
    weekend_info = row.find('td', {'class': 'mojo-field-type-date_interval'}).findChildren()[0]
    film["weekend"] = [weekend_info.getText(), url + weekend_info.get('href')]
    film["realeses"] = int(row.find('td', {'class': 'mojo-field-type-positive_integer'}).getText())

    try:
        frealeses_info = row.find('td', {'class': 'mojo-field-type-release'}).findChildren()[0]
        film["first_realeses"] = [frealeses_info.getText(), url + frealeses_info.get('href')]
    except:
        film["first_realeses"] = None
    try:
        distributor_info = row.find('td', {'class': 'mojo-field-type-studio'}).findChildren()[0]
        film["distributor"] = [frealeses_info.getText(), url + frealeses_info.get('href')]
    except:
        film["distributor"] = None
    film["gross"] = int(row.find('td', {'class': 'mojo-field-type-positive_integer'}).getText())

    films.append(film)




# test_link = soup.find("a", {"class": "a-link-normal"})

pprint(films)

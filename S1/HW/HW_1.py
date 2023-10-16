import requests
from pprint import pprint


url = "https://pokeapi.co/api/v2/pokemon/"

pokemon_id = input("Введите ID Покемона от 1 до 1017: ")

response = requests.get(url + pokemon_id)
j_data = response.json()

name = j_data.get("name")
pokemon_types = []
for typ in j_data.get("types"):
    pokemon_types.append(typ.get("type").get("name"))
height = j_data.get("height")
weight = j_data.get("weight")
pokemon_abilities = []
for ability in j_data.get("abilities"):
    pokemon_abilities.append(ability.get("ability").get("name"))

pokemon = {"Имя": name,
           "Тип": pokemon_types,
           "Рост": height,
           "Вес": weight,
           "Способности": pokemon_abilities}

pprint(pokemon, sort_dicts=False)

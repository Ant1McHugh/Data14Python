import requests
import json
from pprint import pprint

address = "https://pokeapi.co/api/v2/pokemon/pikachu/"
req_response = requests.get(address)
pikachu_ability = req_response.json()['abilities']
list_of_urls = []
list_of_names = []

for ability in pikachu_ability:
    result = ability['ability']
    list_of_names.append(result['name'])
    list_of_urls.append(result['url'])

static_name = list_of_names[0]
lightning_rod_name = list_of_names[1]
static_url = list_of_urls[0]
lightning_rod_url = list_of_urls[1]

static_response = requests.get(static_url)
static_effect = static_response.json()['effect_entries'][1]['short_effect']


lightning_rod_response  = requests.get(lightning_rod_url)
lightning_rod_effect = lightning_rod_response.json()['effect_entries'][1]['short_effect']

print(f"Pikachu can have the ability {static_name}. The effect of this is: {static_effect}")
print(f"Pikachu can have th ability {lightning_rod_name}. The effect of this is:\n{lightning_rod_effect}")


# for url in list_of_abilities:
#     req_response_abilities = requests.get(list_of_abilities[url])
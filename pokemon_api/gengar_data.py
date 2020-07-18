import requests
import json
from pprint import pprint

address = "https://pokeapi.co/api/v2/pokemon/charmander/"
req_response = requests.get(address)
pprint(req_response.json())

# gengar_ability = req_response.json()['abilities']
# list_for_ability = []
# ability_names = []
#
# for ability in gengar_ability:
#     result = ability['ability']
#     ability_names.append(result['name'])
#     list_for_ability.append(result['url'])
#
# ability_url = list_for_ability[0]
#
# ability_response = requests.get(ability_url)
#
# ability_effect = ability_response.json()['effect_entries'][1]
#
# name_of_ability = ability_names[0]
#
# print(f"Gengar's ability is {name_of_ability}. Its effect is: {ability_effect['effect']}")
#
#
#
# gengar_types = req_response.json()['types']
# gengar_type1 = gengar_types[0]['type']
# gengar_type2 = gengar_types[1]['type']
#
# print(f"Gengar has two types. These are {gengar_type1['name']} and {gengar_type2['name']}.")
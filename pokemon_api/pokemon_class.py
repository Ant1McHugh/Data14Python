import requests
import json
from pprint import pprint

class PokeFacts:

    def __init__(self, pokemon):
        self.pokemon_name = pokemon
        self.address = f"https://pokeapi.co/api/v2/pokemon/{pokemon}/" # API with pokemon name as input
        self.req_response = requests.get(self.address) # Accesses th api
        self.ability_list = []
        self.type_list = []
        self.move_list = []
        self.stat_list = []

    def ability_names(self):
        # This method will return the name of abilities available to input pokemon
        pokemon_ability = self.req_response.json()['abilities']
        for ability in pokemon_ability:
            result = ability['ability']
            self.ability_list.append(result['name'])
        print(self.ability_list)

    def type_names(self):
        # This method returns the typings of the input pokemon
        pokemon_type = self.req_response.json()['types']
        for type in pokemon_type:
            result = type['type']
            self.type_list.append(result['name'])
        print(self.type_list)

    def move_names(self):
        # This method produces a list of all moves that the pokemon can learn
        pokemon_moves = self.req_response.json()['moves']
        for move in pokemon_moves:
            result = move['move']
            self.move_list.append(result['name'])
        pprint(self.move_list)

    def pokedex_number(self):
        pokedex_number = self.req_response.json()['id']
        print(pokedex_number)

    def base_stats(self):
        stats_file = self.req_response.json()['stats']
        for row in stats_file:
            self.stat_list.append(f"{row['stat']['name']}: {row['base_stat']}")
        print(self.stat_list)





pokemon = PokeFacts('togekiss')
pokemon.ability_names()
pokemon.base_stats()
pokemon.type_names()
pokemon.pokedex_number()
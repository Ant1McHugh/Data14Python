import json
from pprint import pprint

class JsonStore:

    def __init__(self, jsonfile_name):
        with open(jsonfile_name) as jsonfile:
            film_dict = json.load(jsonfile)
        self.name = film_dict["name"]
    # def create_instance(self):
    #
    #
    # def store_json(self):

film = JsonStore()

film.read_json("film.json")
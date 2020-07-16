import json
from pprint import pprint

class JsonStore:

    def __init__(self, jsonfile_name):
        with open(jsonfile_name) as jsonfile:
            film_dict = json.load(jsonfile)
        self.name = film_dict["name"]
        self.year = film_dict["year"]
        self.studio = film_dict["studio"]

film = JsonStore("film.json")

print(film.name, film.year, film.studio)
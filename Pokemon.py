import requests
import json
import sys
from pprint import pprint

class Pokemon():

    # Variables
    pokemon_base_url = "http://pokeapi.co/api/v2/pokemon/"
    nature_base_url = "http://pokeapi.co/api/v2/nature/"
    stats = {}
    name = ""
    nature = {}
    hp = int
    level = int

    # Constructor Method
    def __init__(self, name, nature, level):
        self.level = level

        # Library Requests
        r = requests.get(self.pokemon_base_url + name).json()

        # Error Handling
        if r == {"detail":"Not found."}:
            print("Invalid Name.")
            sys.exit()
        else:
            self.name = name
            temp_dict =r['stats']
            for x in temp_dict:
                if x['stat']['name'] == 'hp':
                    self.hp = x['base_stat']
                else:
                    self.stats[x['stat']['name']] = x ['base_stat']

        r = requests.get(self.nature_base_url + nature).json()
        if r == {"detail":"Not found."}:
            print("Invalid Name.")
            sys.exit()
        else:
            try:
                self.nature['increased_stat'] = r['increased_stat']['name']
                self.nature['decreased_stat'] = r['decreased_stat']['name']
            except TypeError:
                self.nature['increased_stat'] = 'null'
                self.nature['decreased_stat'] = 'null'
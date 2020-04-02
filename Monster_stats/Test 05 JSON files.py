from random import randint
from random import seed
import json

seed(randint(1, 100))
initiative = {}
npc = {}


def npc_import(name, variable_number):
    json_exten = ".json"
    alph = name + json_exten
    with open(alph) as data_file:
        data = json.load(data_file)
    middle = '["'
    end = '"]'
    hier_1 = middle + input("Input the creature's name") + end
    while True:
       if data.setdefault("name", "blank") == "blank":
           hier_1 = input("Input the creature's name")
           alph = name + middle + hier_1 + end + json_exten
           with open(alph) as json_file:
               data = json.load(json_file)
       else:
           for p in data:
               npc[variable_number] = {"name": "blank", "initiative": 0, "dexterity": 0}
               npc[variable_number]["name"] = data["name"]
               npc[variable_number]["dexterity"] = data["dexterity"]
               npc[variable_number]["initiative"] = randint(1, 20) + int(npc[variable_number]["dexterity"])
               initiative.update({npc[variable_number]["name"]: npc[variable_number]["initiative"]})
           break

variable = input("Input the creature's name")
npc_import(variable, 1)

print(npc[variable])
from random import randint
from random import seed
import json

seed(randint(1, 100))
initiative = {}
npc = {}

#Fully figured out a function for NPC input

def npc_import(name, variable_number):
    def update(dictionary):
        for x in dictionary:
            npc[variable_number] = {"name": "blank", "initiative": 0, "dexterity": 0}
            npc[variable_number]["name"] = dictionary["name"]
            npc[variable_number]["dexterity"] = dictionary["dexterity"]
            npc[variable_number]["initiative"] = randint(1, 20) + int(npc[variable_number]["dexterity"])
            initiative.update({npc[variable_number]["name"]: npc[variable_number]["initiative"]})
    json_exten = ".json"
    alph = name + json_exten
    with open(alph) as data_file:
        data = json.load(data_file)
    dictionary = data
    while True:
       if data.setdefault("name", "blank") == "blank":
           hier_1 = input("Input the creature's name")
           dictionary = data[hier_1]
           if data[hier_1].setdefault("name", "blank") == "blank":
               hier_2 = input("Input the creature's name")
               dictionary = data[hier_1][hier_2]
               if data[hier_1][hier_2].setdefault("name", "blank") == "blank":
                   hier_3 = input("Input the creature's name")
                   dictionary = data[hier_1][hier_2][hier_3]
                   if data[hier_1][hier_2][hier_3].setdefault("name", "blank") == "blank":
                       hier_4 = input("Input the creature's name")
                       dictionary = data[hier_1][hier_2][hier_3][hier_4]
                       if data[hier_1][hier_2][hier_3][hier_4].setdefault("name", "blank") == "blank":
                           print("ERROR!!!")
                       else:
                           update(dictionary)
                           break
                   else:
                       update(dictionary)
                       break
               else:
                   update(dictionary)
                   break
           else:
               update(dictionary)
               break
       else:
           update(dictionary)
           break

variable_number = 1
npcs = int(input("How many NPCs are participating? ")) + 1
for variable_number in range(1, npcs):
    variable = input("Input the creature's name")
    npc_import(variable, variable_number)
    initiative.update({npc[index_value]["name"]: npc[index_value]["initiative"]})
from random import randint
from random import seed
import json

seed(randint(1, 100))
initiative = {}

# NPC VARIABLES
npc = {}
npc["npc1"] = {"name": "blank", "dexterity": 0, "initiative": 0}
npc["npc2"] = {"name": "blank", "dexterity": 0, "initiative": 0}
npc["npc3"] = {"name": "blank", "dexterity": 0, "initiative": 0}
npc["npc4"] = {"name": "blank", "dexterity": 0, "initiative": 0}
npc["npc5"] = {"name": "blank", "dexterity": 0, "initiative": 0}
npc["npc6"] = {"name": "blank", "dexterity": 0, "initiative": 0}
npc["npc7"] = {"name": "blank", "dexterity": 0, "initiative": 0}
npc["npc8"] = {"name": "blank", "dexterity": 0, "initiative": 0}
npc["npc9"] = {"name": "blank", "dexterity": 0, "initiative": 0}
npc["npc10"] = {"name": "blank", "dexterity": 0, "initiative": 0}
npc["npc11"] = {"name": "blank", "dexterity": 0, "initiative": 0}
npc["npc12"] = {"name": "blank", "dexterity": 0, "initiative": 0}
npc["npc13"] = {"name": "blank", "dexterity": 0, "initiative": 0}
npc["npc14"] = {"name": "blank", "dexterity": 0, "initiative": 0}
npc["npc15"] = {"name": "blank", "dexterity": 0, "initiative": 0}

# NPC STATS IMPORT
def npc_import(name, variable_number):
    json_exten = ".json"
    name = name + json_exten
    with open(name) as json_file:
        data = json.load(json_file)
        name
        for p in data['people']:
            npc[variable_number] = {"name": "blank", "initiative": 0, "dexterity": 0}
            npc[variable_number]["name"] = name["name"]
            npc[variable_number]["dexterity"] = name["dexterity"]
            npc[variable_number]["initiative"] = randint(1, 20) + int(name["dexterity"])
            initiative.update({npc[variable_number]["name"]: npc[variable_number]["initiative"]})

i_npc = 1
npcs = int(input("How many NPCs are participating? ")) + 1
for i_npc in range (1, npcs):
    npc_name = input("Input the name of the NPC: ")
    npc_import(npc_name, i_npc)


# PC INFO
#choice = input("Would you like to use an already made set of PCs(Answer y or n)?" )
#if choice == "y":
    #code for importing an already existing json file
#else:
i_pc = 1
pcs = int(input("How many PCs are participating? "))
while i_pc <= pcs:
    players = {}
    value_pc = 'player%d' % i_pc
    players[value_pc] = {"name": "blank", "initiative": 0, "dexterity": 0}
    print("Input information of PC", i_pc)
    players[value_pc]["name"] = input("Name: ")
    players[value_pc]["initiative"] = int(input("Initiative Score: "))
    players[value_pc]["dexterity"] = int(input("Dexterity Modifier: "))
    initiative.update({players[value_pc]["name"]: players[value_pc]["initiative"]})
    file = open("players.json", "w")
    file.write(json.dumps(players))
    file.close()
    i_pc += 1

# UNUSED NPC VARIABLE FILTER

def var_filter(dictionary):
    index_number = 1
    while index_number <= 15:
        index_value = 'npc%d' % index_number
        if npc[index_value]["initiative"] == 0:
            if npc[index_value]["name"] != "blank":
                dictionary.update({npc[index_value]["name"]: npc[index_value]["initiative"]})
        else:
            dictionary.update({npc[index_value]["name"]: npc[index_value]["initiative"]})
        index_number += 1


var_filter(initiative)

# FINAL INITIATIVE LIST SORTING & DISPLAY

a = sorted(initiative.items(), key=lambda x: x[1], reverse=True, indent = 2)
print(a)
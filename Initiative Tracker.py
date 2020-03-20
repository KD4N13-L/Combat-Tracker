from random import randint
from random import seed
import json
seed(randint(1, 100))
initiative = {}

#NPC STATS IMPORT



#NPC VARIABLES

npc1 = {"name": "blank", "dexterity": 0, "initiative": 0}
npc2 = {"name": "blank", "dexterity": 0, "initiative": 0}
npc3 = {"name": "blank", "dexterity": 0, "initiative": 0}
npc4 = {"name": "blank", "dexterity": 0, "initiative": 0}
npc5 = {"name": "blank", "dexterity": 0, "initiative": 0}
npc6 = {"name": "blank", "dexterity": 0, "initiative": 0}
npc7 = {"name": "blank", "dexterity": 0, "initiative": 0}
npc8 = {"name": "blank", "dexterity": 0, "initiative": 0}
npc9 = {"name": "blank", "dexterity": 0, "initiative": 0}
npc10 = {"name": "blank", "dexterity": 0, "initiative": 0}
npc11 = {"name": "blank", "dexterity": 0, "initiative": 0}
npc12 = {"name": "blank", "dexterity": 0, "initiative": 0}
npc13 = {"name": "blank", "dexterity": 0, "initiative": 0}
npc14 = {"name": "blank", "dexterity": 0, "initiative": 0}
npc15 = {"name": "blank", "dexterity": 0, "initiative": 0}

#PC INFO

#Add an IF statement to check if there already exists players information as a json file;
#OR
#Ask the user whether they want to import new characters or use already existing info
#(this option may be deleted if the user is sure they will be using only one json file).

#First time usage, for creating the json file wit PC information
players={}
i = 1
pcs = int(input("How many PCs are participating? "))
while i<=pcs:
    value = 'player%d' % i
    players[value] = {"name": "blank", "initiative": 0, "dexterity": 0}
    print("Input information of PC", i)
    players[value]["name"] = input("Name: ")
    players[value]["initiative"] = int(input("Initiative Score: "))
    players[value]["dexterity"] = int(input("Dexterity Modifier: "))
    initiative.update({players[value]["name"]: players[value]["initiative"]})
    file = open("players.json", "w")
    file.write(json.dumps(players))
    file.close()
    i += 1

#UNUSED NPC VARIABLE FILTER

if npc1["initiative"] == 0:
    if npc1["name"] != "blank":
        initiative.update({npc1["name"]: npc1["initiative"]})
else:
    initiative.update({npc1["name"]: npc1["initiative"]})
if npc2["initiative"] == 0:
    if npc2["name"] != "blank":
        initiative.update({npc2["name"]: npc2["initiative"]})
else:
    initiative.update({npc2["name"]: npc2["initiative"]})
if npc3["initiative"] == 0:
    if npc3["name"] != "blank":
        initiative.update({npc3["name"]: npc3["initiative"]})
else:
    initiative.update({npc3["name"]: npc3["initiative"]})
if npc4["initiative"] == 0:
    if npc4["name"] != "blank":
        initiative.update({npc4["name"]: npc4["initiative"]})
else:
    initiative.update({npc4["name"]: npc4["initiative"]})
if npc5["initiative"] == 0:
    if npc5["name"] != "blank":
        initiative.update({npc5["name"]: npc5["initiative"]})
else:
    initiative.update({npc5["name"]: npc5["initiative"]})
if npc6["initiative"] == 0:
    if npc6["name"] != "blank":
        initiative.update({npc6["name"]: npc6["initiative"]})
else:
    initiative.update({npc6["name"]: npc6["initiative"]})
if npc7["initiative"] == 0:
    if npc7["name"] != "blank":
        initiative.update({npc7["name"]: npc7["initiative"]})
else:
    initiative.update({npc7["name"]: npc7["initiative"]})
if npc8["initiative"] == 0:
    if npc8["name"] != "blank":
        initiative.update({npc8["name"]: npc8["initiative"]})
else:
        initiative.update({npc8["name"]: npc8["initiative"]})
if npc9["initiative"] == 0:
    if npc9["name"] != "blank":
        initiative.update({npc9["name"]: npc9["initiative"]})
else:
        initiative.update({npc9["name"]: npc9["initiative"]})
if npc10["initiative"] == 0:
    if npc10["name"] != "blank":
        initiative.update({npc10["name"]: npc10["initiative"]})
else:
        initiative.update({npc10["name"]: npc10["initiative"]})
if npc11["initiative"] == 0:
    if npc11["name"] != "blank":
        initiative.update({npc11["name"]: npc11["initiative"]})
else:
        initiative.update({npc11["name"]: npc11["initiative"]})
if npc12["initiative"] == 0:
    if npc12["name"] != "blank":
        initiative.update({npc12["name"]: npc12["initiative"]})
else:
        initiative.update({npc12["name"]: npc12["initiative"]})
if npc13["initiative"] == 0:
    if npc13["name"] != "blank":
        initiative.update({npc13["name"]: npc13["initiative"]})
else:
        initiative.update({npc13["name"]: npc13["initiative"]})
if npc14["initiative"] == 0:
    if npc14["name"] != "blank":
        initiative.update({npc14["name"]: npc14["initiative"]})
else:
        initiative.update({npc14["name"]: npc14["initiative"]})
if npc15["initiative"] == 0:
    if npc15["name"] != "blank":
        initiative.update({npc15["name"]: npc15["initiative"]})
else:
        initiative.update({npc15["name"]: npc15["initiative"]})

#FINAL INITIATIVE LIST SORTING & DISPLAY

a = sorted(initiative.items(), key=lambda x:x[1], reverse=True)
print(a)

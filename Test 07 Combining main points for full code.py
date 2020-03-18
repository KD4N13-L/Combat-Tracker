from random import randint
from random import seed
seed(randint(1, 100))

carrion_crawler = {}
carrion_crawler ["name"] = "Carrion Crawler"
carrion_crawler ["dexterity"] = "1"

npc1 = {"name": "blank", "dexterity": 0, "initiative": 0}

npc2 = {"name": "blank", "dexterity": 0, "initiative": 0}

npc3 = {"name": "blank", "dexterity": 0, "initiative": 0}

npc1 ["name"] = carrion_crawler ["name"]
npc1 ["dexterity"] = carrion_crawler ["dexterity"] = "1"
npc1 ["initiative"] = randint(1, 20) + int(npc1 ["dexterity"])

print("Test", npc1 ["initiative"])
print(" ")

print("Input the PC information")

pc1 = {"name": "blank", "initiative": 0, "dexterity": 0}

pc2 = {}
pc2 ["name"] = "blank"
pc2 ["initiative"] = 0
pc2 ["dexterity"] = 0

print ("PC1:")

pc1["name"] = input("Name: ")
pc1["initiative"] = int(input("Initiative Score: "))
pc1["dexterity"] = int(input("Dexterity Modifier: "))

print ("PC2:")

pc2["name"] = input("Name: ")
pc2["initiative"] = int(input("Initiative Score: "))
pc2["dexterity"] = int(input("Dexterity Modifier: "))

initiative = {}

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

if pc1["initiative"] == 0:
    if pc1["name"] != "blank":
        initiative.update({pc1["name"]: pc1["initiative"]})
else:
    initiative.update({pc1["name"]: pc1["initiative"]})

if pc2["initiative"] == 0:
    if pc2["name"] != "blank":
        initiative.update({pc2["name"]: pc2["initiative"]})
else:
    initiative.update({pc2["name"]: pc2["initiative"]})

a = sorted(initiative.items(), key=lambda x:x[1], reverse=True)

print(a)
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
print("      print("Input the PC information")

pc1 = {"name": "blank", "dexterity": 0, "initiative": 0}
pc2 = {"name": "blank", "dexterity": 0, "initiative": 0}
pc3 = {"name": "blank", "dexterity": 0, "initiative": 0}
pc4 = {"name": "blank", "dexterity": 0, "initiative": 0}
pc5 = {"name": "blank", "dexterity": 0, "initiative": 0}
pc6 = {"name": "blank", "dexterity": 0, "initiative": 0}
pc7 = {"name": "blank", "dexterity": 0, "initiative": 0}

print("Input the PC information")

t = True
while t:
    print("PC1:")
    pc1["name"] = input("Name: ")
    pc1["initiative"] = int(input("Initiative Score: "))
    pc1["dexterity"] = int(input("Dexterity Modifier: "))
    cont = input("Do you have more PCs? y/n")
    if cont == "n":
        break

    print ("PC2:")
    pc2["name"] = input("Name: ")
    pc2["initiative"] = int(input("Initiative Score: "))
    pc2["dexterity"] = int(input("Dexterity Modifier: "))
    cont = input("Do you have more PCs? y/n")
    if cont == "n":
        break

    print ("PC3:")
    pc3["name"] = input("Name: ")
    pc3["initiative"] = int(input("Initiative Score: "))
    pc3["dexterity"] = int(input("Dexterity Modifier: "))
    cont = input("Do you have more PCs? y/n")
    if cont == "n":
        break

    print ("PC4:")
    pc4["name"] = input("Name: ")
    pc4["initiative"] = int(input("Initiative Score: "))
    pc4["dexterity"] = int(input("Dexterity Modifier: "))
    cont = input("Do you have more PCs? y/n")
    if cont == "n":
        break

    print ("PC5:")
    pc5["name"] = input("Name: ")
    pc5["initiative"] = int(input("Initiative Score: "))
    pc5["dexterity"] = int(input("Dexterity Modifier: "))
    cont = input("Do you have more PCs? y/n")
    if cont == "n":
        break

    print ("PC6:")
    pc6["name"] = input("Name: ")
    pc6["initiative"] = int(input("Initiative Score: "))
    pc6["dexterity"] = int(input("Dexterity Modifier: "))
    cont = input("Do you have more PCs? y/n")
    if cont == "n":
        break

    print("PC7:")
    pc7["name"] = input("Name: ")
    pc7["initiative"] = int(input("Initiative Score: "))
    pc7["dexterity"] = int(input("Dexterity Modifier: "))
    cont = input("Do you have more PCs? y/n")
    if cont == "n":
        break

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
if pc3["initiative"] == 0:
    if pc3["name"] != "blank":
        initiative.update({pc3["name"]: pc3["initiative"]})
else:
    initiative.update({pc3["name"]: pc3["initiative"]})
if pc4["initiative"] == 0:
    if pc4["name"] != "blank":
        initiative.update({pc4["name"]: pc4["initiative"]})
else:
    initiative.update({pc4["name"]: pc4["initiative"]})
if pc5["initiative"] == 0:
    if pc5["name"] != "blank":
        initiative.update({pc5["name"]: pc5["initiative"]})
else:
    initiative.update({pc5["name"]: pc5["initiative"]})
if pc6["initiative"] == 0:
    if pc6["name"] != "blank":
        initiative.update({pc6["name"]: pc6["initiative"]})
else:
    initiative.update({pc6["name"]: pc6["initiative"]})
if pc7["initiative"] == 0:
    if pc7["name"] != "blank":
        initiative.update({pc7["name"]: pc7["initiative"]})
else:
    initiative.update({pc7["name"]: pc7["initiative"]})

a = sorted(initiative.items(), key=lambda x:x[1], reverse=True)

print(a)
from random import randint
from random import seed
seed(randint(1, 100))


npc1 = {"name": "blank", "dexterity": 0, "initiative": 0}
npc2 = {"name": "blank", "dexterity": 0, "initiative": 0}
npc3 = {"name": "blank", "dexterity": 0, "initiative": 0}

npc1 ["name"] = carrion_crawler ["name"]
npc1 ["dexterity"] = carrion_crawler ["dexterity"] = "1"
npc1 ["initiative"] = randint(1, 20) + int(npc1 ["dexterity"])

print("Test", npc1 ["initiative"])
print("Input the PC information")

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
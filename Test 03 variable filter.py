fungi_violet_fungus = {}
fungi_violet_fungus ["name"] = "Violet Fungus"
fungi_violet_fungus ["dexterity"] = "-5"

npc1 = {}
npc1 ["name"] = fungi_violet_fungus ["name"]
npc1 ["initiative"] = 8 + int(fungi_violet_fungus["dexterity"])

npc2 = {}
npc2 ["name"] = fungi_violet_fungus ["name"]
npc2 ["initiative"] = 5 + int(fungi_violet_fungus["dexterity"])

npc3 = {}
npc3 ["name"] = "blank"
npc3 ["initiative"] = 0

if (npc1["initiative"] == 0):
    if (npc1["name"] != "blank"):
        print (npc1["name"], ": ", npc1["initiative"])
else:
    print (npc1["name"], ": ", npc1["initiative"])

if (npc2["initiative"] == 0):
    if (npc2["name"] != "blank"):
        print (npc2["name"], ": ", npc2["initiative"])
else:
    print (npc2["name"], ": ", npc2["initiative"])

if (npc3["initiative"] == 0):
    if (npc3["name"] != "blank"):
        print (npc3["name"], ": ", npc3["initiative"])
else:
    print (npc3["name"], ": ", npc3["initiative"])
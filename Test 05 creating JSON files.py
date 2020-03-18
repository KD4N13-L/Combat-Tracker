import json

fungi_violet_fungus = {}
fungi_violet_fungus ["name"] = "Violet Fungus"
fungi_violet_fungus ["dexterity"] = "-5"

file = open("fungi_violet_fungus.json", "w")
file.write(json.dumps(fungi_violet_fungus))
file.close()

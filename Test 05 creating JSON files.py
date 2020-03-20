import json

b={}
b["beholder"] = {}
b["blight"] = {}
b["bugbear"] = {}

b["banshee"] = {"name": "Banshee", "dexterity": "2"}

b["basilisk"] = {"name": "Basilisk", "dexterity": "-1"}

b["behir"] = {"name": "Behir", "dexterity": "3"}

b["beholder"] = {"name": "Beholder", "dexterity": "2"}

b["beholder"]["death_tyrant"] = {"name": "Death Tyrant", "dexterity": "2"}

b["beholder"]["spectator"] = {"name": "Spectator", "dexterity": "2"}

b["blight"]["needle"] = {"name": "Needle Blight", "dexterity": "1"}

b["blight"]["twig"] = {"name": "Twig Blight", "dexterity": "1"}

b["blight"]["vine"] = {"name": "Vine Blight", "dexterity": "-1"}

b["bugbear"] = {"name": "Bugbear", "dexterity": "2"}

b["bugbear"]["chief"] = {"name": "Bugbear Chief", "dexterity": "2"}

b["bullete"] = {"name": "Bullete", "dexterity": "0"}

b["bullywug"] = {"name": "Bullywug", "dexterity": "1"}

with open("Monter stats/b.json", "w") as f:
    json.dump(b, f, sort_keys=True, indent=1)

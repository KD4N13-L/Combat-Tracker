import json

# Monster Manual
a = {}
a["angel"] = {}
a["animated"] = {}

a["aarakocra"] = {"name": "Aarakocra", "dexterity": "2"}
a["aboleth"] = {"name": "Aboleth", "dexterity": "-1"}
a["angel"]["deva"] = {"name": "Deva", "dexterity": "4"}
a["angel"]["planetar"] = {"name": "Planetar", "dexterity": "5"}
a["angel"]["solar"] = {"name": "Solar", "dexterity": "6"}
a["animated"]["armor"] = {"name": "Animanted Armor", "dexterity": "0"}
a["animated"]["flying_sword"] = {"name": "Flying Sword", "dexterity": "2"}
a["animated"]["rug_of_smothering"] = {"name": "Rug of Smothering", "dexterity": "2"}
a["ankheg"] = {"name": "Ankheg", "dexterity": "0"}
a["azer"] = {"name": "Azer", "dexterity": "1"}

b = {}
b["beholder"] = {}
b["blight"] = {}
b["bugbear"] = {}

b["banshee"] = {"name": "Banshee", "dexterity": "2"}
b["basilisk"] = {"name": "Basilisk", "dexterity": "-1"}
b["behir"] = {"name": "Behir", "dexterity": "3"}
b["beholder"]["regular"] = {"name": "Beholder", "dexterity": "2"}
b["beholder"]["death_tyrant"] = {"name": "Death Tyrant", "dexterity": "2"}
b["beholder"]["spectator"] = {"name": "Spectator", "dexterity": "2"}
b["blight"]["needle"] = {"name": "Needle Blight", "dexterity": "1"}
b["blight"]["twig"] = {"name": "Twig Blight", "dexterity": "1"}
b["blight"]["vine"] = {"name": "Vine Blight", "dexterity": "-1"}
b["bugbear"]["regular"] = {"name": "Bugbear", "dexterity": "2"}
b["bugbear"]["chief"] = {"name": "Bugbear Chief", "dexterity": "2"}
b["bullete"] = {"name": "Bullete", "dexterity": "0"}
b["bullywug"] = {"name": "Bullywug", "dexterity": "1"}

c = {}

c["cambion"] = {"name": "Cambion", "dexterity": "4"}
c["carrion_crawler"] = {"name": "Carrion Crawler", "dexterity": "1"}
c["centaur"] = {"name": "Centaur", "dexterity": "2"}
c["chimera"] = {"name": "Chimera", "dexterity": "0"}
c["chuul"] = {"name": "Chuul", "dexterity": "0"}
c["cloaker"] = {"name": "Cloaker", "dexterity": "2"}
c["cockatrice"] = {"name": "Cockatrice", "dexterity": "1"}
c["couatl"] = {"name": "Couatl", "dexterity": "5"}
c["crawling_claw"] = {"name": "Crawling Claw", "dexterity": "2"}
c["cyclops"] = {"name": "Cyclops", "dexterity": "0"}

d = {}
d["demon"] = {}
d["devil"] = {}
d["dinosaur"] = {}
d["dragon"] = {}
d["dragon"]["red"] = {}
d["dragon"]["black"] = {}
d["dragon"]["blue"] = {}
d["dragon"]["green"] = {}
d["dragon"]["red"] = {}
d["dragon"]["red"]["shadow"] = {}
d["dragon"]["white"] = {}
d["dragon"]["brass"] = {}
d["dragon"]["bronze"] = {}
d["dragon"]["copper"] = {}
d["dragon"]["gold"] = {}
d["dragon"]["silver"] = {}

d["darkmantle"] = {"name": "Darkmantle", "dexterity": "1"}
d["death_knight"] = {"name": "Death Knight", "dexterity": "0"}
d["demilich"] = {"name": "Demilich", "dexterity": "5"}
d["demon"]["balor"] = {"name": "Balor", "dexterity": "2"}
d["demon"]["barlgura"] = {"name": "Barlgura", "dexterity": "2"}
d["demon"]["chasme"] = {"name": "Chasme", "dexterity": "2"}
d["demon"]["dretch"] = {"name": "Dretch", "dexterity": "0"}
d["demon"]["glabrezu"] = {"name": "Glabrezu", "dexterity": "2"}
d["demon"]["goristro"] = {"name": "Goristro", "dexterity": "0"}
d["demon"]["hezrou"] = {"name": "Hezrou", "dexterity": "3"}
d["demon"]["manes"] = {"name": "Manes", "dexterity": "-1"}
d["demon"]["marilith"] = {"name": "Marilith", "dexterity": "2"}
d["demon"]["nalfeshnee"] = {"name": "Nalfeshnee", "dexterity": "2"}
d["demon"]["quasit"] = {"name": "Quasit", "dexterity": "3"}
d["demon"]["shadow_demon"] = {"name": "Shadow Demon", "dexterity": "3"}
d["demon"]["vrock"] = {"name": "Vrock", "dexterity": "2"}
d["demon"]["yochlol"] = {"name": "Yochlol", "dexterity": "2"}
d["devil"]["barbed_devil"] = {"name": "Barbed Devil (Hamatula)", "dexterity": "3"}
d["devil"]["bearded_devil"] = {"name": "Bearded Devil (Barbazu)", "dexterity": "2"}
d["devil"]["bone_devil"] = {"name": "Bone Devil (Osyluth)", "dexterity": "3"}
d["devil"]["chain_devil"] = {"name": "Chain Devil (Kyton)", "dexterity": "2"}
d["devil"]["erinyes"] = {"name": "Erinyes", "dexterity": "3"}
d["devil"]["horned_devil"] = {"name": "Horned Devil (Malebranche)", "dexterity": "3"}
d["devil"]["ice_devil"] = {"name": "Ice Devil (Gelugon)", "dexterity": "2"}
d["devil"]["imp"] = {"name": "Imp", "dexterity": "3"}
d["devil"]["lemure"] = {"name": "Lemure", "dexterity": "-3"}
d["devil"]["pit_fiend"] = {"name": "Pit Fiend", "dexterity": "2"}
d["devil"]["spined_devil"] = {"name": "Spined Devil (Spinagon)", "dexterity": "2"}
d["dinosaur"]["allosaurus"] = {"name": "Alloaurus", "dexterity": "1"}
d["dinosaur"]["ankylosaurus"] = {"name": "Ankylosaurus", "dexterity": "0"}
d["dinosaur"]["plesiosaurus"] = {"name": "Plesiosaurus", "dexterity": "2"}
d["dinosaur"]["pteranodon"] = {"name": "Pteranodon", "dexterity": "2"}
d["dinosaur"]["triceratops"] = {"name": "Triceratops", "dexterity": "-1"}
d["dinosaur"]["tyrannosaurus_rex"] = {"name": "Tyrannosaurus Rex", "dexterity": "0"}
d["displacer_beast"] = {"name": "Displacer Beast", "dexterity": "2"}
d["doppelganger"] = {"name": "Doppelganger", "dexterity": "4"}
d["dracolich_adult_blue"] = {"name": "Adult Blue Dracolich", "dexterity": "0"}
d["dragon"]["red"]["shadow"]["young"] = {"name": "Young Red Shadow Dragon", "dexterity": "0"}
d["dragon"]["black"]["ancient"] = {"name": "Ancient Black Dragon", "dexterity": "2"}
d["dragon"]["black"]["adult"] = {"name": "Adult Black Dragon", "dexterity": "2"}
d["dragon"]["black"]["young"] = {"name": "Young Black Dragon", "dexterity": "2"}
d["dragon"]["black"]["wyrmling"] = {"name": "Black Dragon Wyrmling", "dexterity": "2"}
d["dragon"]["blue"]["ancient"] = {"name": "Ancient Blue Dragon", "dexterity": "0"}
d["dragon"]["blue"]["adult"] = {"name": "Adult Blue Dragon", "dexterity": "0"}
d["dragon"]["blue"]["young"] = {"name": "Young Blue Dragon", "dexterity": "0"}
d["dragon"]["blue"]["wyrmling"] = {"name": "Blue Dragon Wyrmling", "dexterity": "0"}
d["dragon"]["green"]["ancient"] = {"name": "Ancient Green Dragon", "dexterity": "1"}
d["dragon"]["green"]["adult"] = {"name": "Adult Green Dragon", "dexterity": "1"}
d["dragon"]["green"]["young"] = {"name": "Young Green Dragon", "dexterity": "1"}
d["dragon"]["green"]["wyrmling"] = {"name": "Green Dragon Wyrmling", "dexterity": "1"}
d["dragon"]["red"]["ancient"] = {"name": "Ancient Red Dragon", "dexterity": "0"}
d["dragon"]["red"]["adult"] = {"name": "Adult Red Dragon", "dexterity": "0"}
d["dragon"]["red"]["young"] = {"name": "Young Red Dragon", "dexterity": "0"}
d["dragon"]["red"]["wyrmling"] = {"name": "Red Dragon Wyrmling", "dexterity": "0"}
d["dragon"]["white"]["ancient"] = {"name": "Ancient White Dragon", "dexterity": "0"}
d["dragon"]["white"]["adult"] = {"name": "Adult White Dragon", "dexterity": "0"}
d["dragon"]["white"]["young"] = {"name": "Young White Dragon", "dexterity": "0"}
d["dragon"]["white"]["wyrmling"] = {"name": "White Dragon Wyrmling", "dexterity": "0"}
d["dragon"]["brass"]["ancient"] = {"name": "Ancient Brass Dragon", "dexterity": "0"}
d["dragon"]["brass"]["adult"] = {"name": "Adult Brass Dragon", "dexterity": "0"}
d["dragon"]["brass"]["young"] = {"name": "Young Brass Dragon", "dexterity": "0"}
d["dragon"]["brass"]["wyrmling"] = {"name": "Brass Dragon Wyrmling", "dexterity": "0"}
d["dragon"]["bronze"]["ancient"] = {"name": "Ancient Bronze Dragon", "dexterity": "0"}
d["dragon"]["bronze"]["adult"] = {"name": "Adult Bronze Dragon", "dexterity": "0"}
d["dragon"]["bronze"]["young"] = {"name": "Young Bronze Dragon", "dexterity": "0"}
d["dragon"]["bronze"]["wyrmling"] = {"name": "Bronze Dragon Wyrmling", "dexterity": "0"}
d["dragon"]["copper"]["ancient"] = {"name": "Ancient Copper Dragon", "dexterity": "1"}
d["dragon"]["copper"]["adult"] = {"name": "Adult Copper Dragon", "dexterity": "1"}
d["dragon"]["copper"]["young"] = {"name": "Young Copper Dragon", "dexterity": "1"}
d["dragon"]["copper"]["wyrmling"] = {"name": "Copper Dragon Wyrmling", "dexterity": "1"}
d["dragon"]["gold"]["ancient"] = {"name": "Ancient Gold Dragon", "dexterity": "2"}
d["dragon"]["gold"]["adult"] = {"name": "Adult Gold Dragon", "dexterity": "2"}
d["dragon"]["gold"]["young"] = {"name": "Young Gold Dragon", "dexterity": "2"}
d["dragon"]["gold"]["wyrmling"] = {"name": "Gold Dragon Wyrmling", "dexterity": "2"}
d["dragon"]["silver"]["ancient"] = {"name": "Ancient Silver Dragon", "dexterity": "0"}
d["dragon"]["silver"]["adult"] = {"name": "Adult Silver Dragon", "dexterity": "0"}
d["dragon"]["silver"]["young"] = {"name": "Young Silver Dragon", "dexterity": "0"}
d["dragon"]["silver"]["wyrmling"] = {"name": "Silver Dragon Wyrmling", "dexterity": "0"}
d["dragon_turtle"] = {"name": "Dragon Turtle", "dexterity": "0"}
d["drider"] = {"name": "Drider", "dexterity": "3"}
d["dryad"] = {"name": "Dryad", "dexterity": "1"}
d["duergar"] = {"name": "Duergar", "dexterity": "0"}

e = {}
e["elemental"] = {}
e["drow"] = {}

e["elemental"]["air"] = {"name": "Air Elemental", "dexterity": "5"}
e["elemental"]["earth"] = {"name": "Earth Elemental", "dexterity": "-1"}
e["elemental"]["fire"] = {"name": "Fire Elemental", "dexterity": "3"}
e["elemental"]["water"] = {"name": "Water Elemental", "dexterity": "2"}
e["drow"]["regular"] = {"name": "Drow", "dexterity": "2"}
e["drow"]["elite_warrior"] = {"name": "Drow Elite Warrior", "dexterity": "4"}
e["drow"]["mage"] = {"name": "Drow Mage", "dexterity": "2"}
e["drow"]["priestess_of_lolth"] = {"name": "Drow Priestess of Lolth", "dexterity": "2"}
e["empyrean"] = {"name": "Empyrean", "dexterity": "5"}
e["ettercap"] = {"name": "Ettercap", "dexterity": "2"}
e["ettin"] = {"name": "Ettin", "dexterity": "-1"}

f = {}
f["fungi"] = {}

f["faerie_dragon"] = {"name": "Faerie Dragon", "dexterity": "20"}
f["flameskull"] = {"name": "Flameskull", "dexterity": "3"}
f["flumph"] = {"name": "Flumph", "dexterity": "2"}
f["fomorian"] = {"name": "Fomorian", "dexterity": "0"}
f["fungi"]["gas_spore"] = {"name": "Gas Spore", "dexterity": "-5"}
f["fungi"]["shrieker"] = {"name": "Shrieker", "dexterity": "-5"}
f["fungi"]["violet_fungus"] = {"name": "Violet Fungus", "dexterity": "-5"}

g = {}
g["genie"] = {}
g["ghoul"] = {}
g["giant"] = {}
g["githyanki"] = {}
g["githzerai"] = {}
g["gnoll"] = {}
g["goblin"] = {}
g["golem"] = {}
g["grick"] = {}

g["galeb_duhr"] = {"name": "Galeb Duhr", "dexterity": "2"}
g["gargoyle"] = {"name": "Gargoyle", "dexterity": "0"}
g["genie"]["dao"] = {"name": "Dao", "dexterity": "1"}
g["genie"]["djinni"] = {"name": "Djinni", "dexterity": "2"}
g["genie"]["efreeti"] = {"name": "Efreeti", "dexterity": "1"}
g["genie"]["marid"] = {"name": "Marid", "dexterity": "1"}
g["ghost"] = {"name": "Ghost", "dexterity": "1"}
g["ghoul"]["ghast"] = {"name": "Ghast", "dexterity": "3"}
g["ghoul"]["regular"] = {"name": "Ghoul", "dexterity": "2"}
g["giant"]["cloud"] = {"name": "Cloud Giant", "dexterity": "0"}
g["giant"]["fire"] = {"name": "Fire Giant", "dexterity": "-1"}
g["giant"]["frost"] = {"name": "Frost Giant", "dexterity": "-1"}
g["giant"]["hill"] = {"name": "Hill Giant", "dexterity": "-1"}
g["giant"]["stone"] = {"name": "Stone Giant", "dexterity": "2"}
g["giant"]["storm"] = {"name": "Storm Giant", "dexterity": "2"}
g["gibbering_mouther"] = {"name": "Gibbering Mouther", "dexterity": "-1"}
g["githyanki"]["warrior"] = {"name": "Githyanki Warrior", "dexterity": "2"}
g["githyanki"]["knight"] = {"name": "Githyanki Knight", "dexterity": "2"}
g["githzerai"]["monk"] = {"name": "Githzerai Monk", "dexterity": "2"}
g["githzerai"]["zerth"] = {"name": "Githzerai Zerth", "dexterity": "4"}
g["gnoll"]["regular"] = {"name": "Gnoll", "dexterity": "1"}
g["gnoll"]["pack_lord"] = {"name": "Gnoll Pack Lord", "dexterity": "2"}
g["gnoll"]["fang_of_yeenoghu"] = {"name": "Gnoll Fang of Yeenoghu", "dexterity": "2"}
g["gnome_deep_svirfneblin"] = {"name": "Deep Gnome (Svirfneblin)", "dexterity": "2"}
g["goblin"]["regular"] = {"name": "Goblin", "dexterity": "2"}
g["goblin"]["boss"] = {"name": "Goblin Boss", "dexterity": "2"}
g["golem"]["clay"] = {"name": "Clay Golem", "dexterity": "-1"}
g["golem"]["flesh"] = {"name": "Flesh Golem", "dexterity": "-1"}
g["golem"]["iron"] = {"name": "Iron Golem", "dexterity": "-1"}
g["golem"]["stone"] = {"name": "Stone Golem", "dexterity": "-1"}
g["gorgon"] = {"name": "Gorgon", "dexterity": "0"}
g["grell"] = {"name": "Grell", "dexterity": "2"}
g["grick"]["regular"] = {"name": "Grick", "dexterity": "2"}
g["grick"]["alpha"] = {"name": "Grick Alpha", "dexterity": "3"}
g["griffon"] = {"name": "Griffon", "dexterity": "2"}
g["grimlock"] = {"name": "Grimlock", "dexterity": "1"}

h = {}
h["hag"] = {}
h["hobgoblin"] = {}

h["hag"]["green"] = {"name": "Green Hag", "dexterity": "1"}
h["hag"]["night"] = {"name": "Night Hag", "dexterity": "2"}
h["hag"]["sea"] = {"name": "Sea Hag", "dexterity": "1"}
h["half_dragon_red_veteran"] = {"name": "Half-Red Dragon Veteran", "dexterity": "1"}
h["harpy"] = {"name": "Harpy", "dexterity": "1"}
h["hell_hound"] = {"name": "Hell Hound", "dexterity": "1"}
h["helmed_horror"] = {"name": "Helmed Horror", "dexterity": "1"}
h["hippogriff"] = {"name": "Hippogriff", "dexterity": "1"}
h["hobgoblin"]["regular"] = {"name": "Hobgoblin", "dexterity": "1"}
h["hobgoblin"]["captain"] = {"name": "Hobgoblin Captain", "dexterity": "2"}
h["hobgoblin"]["warlord"] = {"name": "Hobgoblin Warlord", "dexterity": "2"}
h["homunculus"] = {"name": "Homunculus", "dexterity": "2"}
h["hook_horror"] = {"name": "Hook Horror", "dexterity": "0"}
h["hydra"] = {"name": "Hydra", "dexterity": "1"}

i = {}

i["intellect_devourer"] = {"name": "Intellect Devourer", "dexterity": "2"}
i["invisible_stalker"] = {"name": "Invisible Stalker", "dexterity": "4"}

j = {}

j["jackalwere"] = {"name": "Jackalwere", "dexterity": "2"}

k = {}
k["kobold"] = {}
k["kuotoa"] = {}

k["kenku"] = {"name": "kenku", "dexterity": "3"}
k["kobold"]["regular"] = {"name": "Kobold", "dexterity": "2"}
k["kobold"]["winged"] = {"name": "Winged Kobold", "dexterity": "3"}
k["kraken"] = {"name": "Kraken", "dexterity": "0"}
k["kuotoa"]["regular"] = {"name": "Kuo-toa", "dexterity": "0"}
k["kuotoa"]["archpriest"] = {"name": "Kuo-toa Archpriest", "dexterity": "2"}
k["kuotoa"]["whip"] = {"name": "Kuo-toa Whip", "dexterity": "0"}

l = {}
l["lizardfolk"] = {}
l["lycanthrope"] = {}

l["lamia"] = {"name": "Lamia", "dexterity": "1"}
l["lich"] = {"name": "Lich", "dexterity": "3"}
l["lizardfolk"]["regular"] = {"name": "Lizardfolk", "dexterity": "0"}
l["lizardfolk"]["shaman"] = {"name": "Lizardfolk Shaman", "dexterity": "0"}
l["lizardfolk"]["king_queen"] = {"name": "Lizard King/Queen", "dexterity": "1"}
l["lycanthrope"]["werebear"] = {"name": "Werebear", "dexterity": "0"}
l["lycanthrope"]["wereboar"] = {"name": "Wereboar", "dexterity": "0"}
l["lycanthrope"]["wererat"] = {"name": "Wererat", "dexterity": "0"}
l["lycanthrope"]["weretiger"] = {"name": "Weretiger", "dexterity": "0"}
l["lycanthrope"]["werewolf"] = {"name": "Werewolf", "dexterity": "0"}

m = {}
m["mephit"] = {}
m["modrone"] = {}
m["mummy"] = {}
m["myconid"] = {}

m["magmin"] = {"name": "Magmin", "dexterity": "2"}
m["manticore"] = {"name": "Manticore", "dexterity": "3"}
m["medusa"] = {"name": "Medusa", "dexterity": "2"}
m["mephit"]["dust"] = {"name": "Dust Mephit", "dexterity": "2"}
m["mephit"]["ice"] = {"name": "Ice Mephit", "dexterity": "1"}
m["mephit"]["magma"] = {"name": "Magma Mephit", "dexterity": "1"}
m["mephit"]["mud"] = {"name": "Mud Mephit", "dexterity": "1"}
m["mephit"]["smoke"] = {"name": "Smoke Mephit", "dexterity": "2"}
m["mephit"]["steam"] = {"name": "Steam Mephit", "dexterity": "0"}
m["merfolk"] = {"name": "Merfolk", "dexterity": "1"}
m["merrow"] = {"name": "Merrow", "dexterity": "0"}
m["mimic"] = {"name": "Mimic", "dexterity": "1"}
m["mind_flayer"] = {"name": "Mind Flayer (illithids)", "dexterity": "1"}
m["minotaur"] = {"name": "Minotaur", "dexterity": "0"}
m["modrone"]["mono"] = {"name": "Monodrone", "dexterity": "1"}
m["modrone"]["duo"] = {"name": "Duodrone", "dexterity": "1"}
m["modrone"]["tri"] = {"name": "Tridrone", "dexterity": "1"}
m["modrone"]["quad"] = {"name": "Quadrone", "dexterity": "2"}
m["modrone"]["penta"] = {"name": "Pentadrone", "dexterity": "2"}
m["mummy"]["regular"] = {"name": "Mummy", "dexterity": "-1"}
m["mummy"]["lord"] = {"name": "Mummy Lord", "dexterity": "0"}
m["myconid"]["sprout"] = {"name": "Myconid Sprout", "dexterity": "0"}
m["myconid"]["quaggoth_spore_servant"] = {"name": "Quaggoth Spore Servant", "dexterity": "1"}
m["myconid"]["adult"] = {"name": "Myconid Adult", "dexterity": "0"}
m["myconid"]["sovereign"] = {"name": "Myconid Sovereign", "dexterity": "0"}

n = {}
n["naga"] = {}

n["naga"]["bone"] = {"name": "Bone Naga", "dexterity": "3"}
n["naga"]["spirit"] = {"name": "Spirit Naga", "dexterity": "3"}
n["naga"]["guardian"] = {"name": "Guardian Naga", "dexterity": "4"}
n["nightmare"] = {"name": "Nightmare", "dexterity": "2"}
n["nothic"] = {"name": "Nothic", "dexterity": "3"}

o = {}
o["ogre"] = {}
o["ooze"] = {}
o["orc"] = {}

o["ogre"]["regular"] = {"name": "Ogre", "dexterity": "-1"}
o["ogre"]["half"] = {"name": "Half-Ogre (Ogrillon)", "dexterity": "0"}
o["oni"] = {"name": "Oni", "dexterity": "0"}
o["ooze"]["black_pudding"] = {"name": "Black Pudding", "dexterity": "-3"}
o["ooze"]["gelationous_cube"] = {"name": "Gelatinous Cube", "dexterity": "-4"}
o["ooze"]["gray"] = {"name": "Gray Ooze", "dexterity": "-2"}
o["ooze"]["ochre_jelly"] = {"name": "Ochre Jelly", "dexterity": "-2"}
o["orc"]["regular"] = {"name": "Orc", "dexterity": "1"}
o["orc"]["war_chief"] = {"name": "Orc War Chief", "dexterity": "1"}
o["orc"]["eye_of_gruumsh"] = {"name": "Orc Eye of Gruumsh", "dexterity": "1"}
o["orc"]["orog"] = {"name": "Orog", "dexterity": "1"}
o["otyugh"] = {"name": "Otyugh", "dexterity": "0"}
o["owlbear"] = {"name": "Owlbear", "dexterity": "1"}

p = {}

p["pegasus"] = {"name": "Pegasus", "dexterity": "2"}
p["peryton"] = {"name": "Peryton", "dexterity": "1"}
p["piercer"] = {"name": "Piercer", "dexterity": "1"}
p["pixie"] = {"name": "Pixie", "dexterity": "5"}
p["pseudodragon"] = {"name": "Pseudodragon", "dexterity": "2"}
p["purple_worm"] = {"name": "Purple Worm", "dexterity": "-2"}

q = {}

q["quaggoth"] = {"name": "Quaggoth", "dexterity": "1"}

r = {}
r["remorhaz"] = {}

r["rakshasa"] = {"name": "Rakshasa", "dexterity": "3"}
r["remorhaz"]["young"] = {"name": "Young Remorhaz", "dexterity": "1"}
r["remorhaz"]["regular"] = {"name": "Remorhaz", "dexterity": "1"}
r["revenant"] = {"name": "Revenant", "dexterity": "2"}
r["roc"] = {"name": "Roc", "dexterity": "0"}
r["roper"] = {"name": "Roper", "dexterity": "-1"}
r["rust_monster"] = {"name": "Rust Monster", "dexterity": "1"}

s = {}
s["sahuagin"] = {}
s["salamander"] = {}
s["skeleton"] = {}
s["slaad"] = {}
s["sphinx"] = {}

s["sahuagin"]["regular"] = {"name": "Sahuagin", "dexterity": "0"}
s["sahuagin"]["priestess"] = {"name": "Sahuagin Priestess", "dexterity": "0"}
s["sahuagin"]["baron"] = {"name": "Sahuagin Baron", "dexterity": "2"}
s["salamander"]["fire_snake"] = {"name": "Fire Snake", "dexterity": "2"}
s["salamander"]["regular"] = {"name": "Salamander", "dexterity": "2"}
s["satyr"] = {"name": "Satyr", "dexterity": "3"}
s["scarecrow"] = {"name": "Scarecrow", "dexterity": "1"}
s["shadow"] = {"name": "Shadow", "dexterity": "2"}
s["shambling_mound"] = {"name": "Shambling Mound", "dexterity": "-1"}
s["shield_guardian"] = {"name": "Shield Guardian", "dexterity": "-1"}
s["skeleton"]["regular"] = {"name": "Skeleton", "dexterity": "2"}
s["skeleton"]["minotaur"] = {"name": "Minotaur Skeleton", "dexterity": "0"}
s["skeleton"]["warhorse"] = {"name": "Warhorse Skeleton", "dexterity": "1"}
s["slaad"]["red"] = {"name": "Red Slaad", "dexterity": "1"}
s["slaad"]["blue"] = {"name": "Blue Slaad", "dexterity": "2"}
s["slaad"]["green"] = {"name": "Green Slaad", "dexterity": "2"}
s["slaad"]["gray"] = {"name": "Gray Slaad", "dexterity": "3"}
s["slaad"]["death"] = {"name": "Death Slaad", "dexterity": "2"}
s["slaad"]["tadpole"] = {"name": "Slaad Tadpole", "dexterity": "2"}
s["specter"] = {"name": "Specter", "dexterity": "2"}
s["sphinx"]["andro"] = {"name": "Androsphinx", "dexterity": "0"}
s["sphinx"]["gyno"] = {"name": "Gynosphinx", "dexterity": "2"}
s["sprite"] = {"name": "sprite", "dexterity": "4"}
s["stirge"] = {"name": "Stirge", "dexterity": "3"}
s["succubus_incubus"] = {"name": "Succubus/Incubus", "dexterity": "3"}

t = {}

t["tarrasque"] = {"name": "Tarrasque", "dexterity": "0"}
t["thrikreen"] = {"name": "Thri-kreen", "dexterity": "2"}
t["treant"] = {"name": "Treant", "dexterity": "-1"}
t["troglodyte"] = {"name": "Troglodyte", "dexterity": "0"}
t["troll"] = {"name": "Troll", "dexterity": "1"}

u = {}

u["umber_hulk"] = {"name": "Umber Hulk", "dexterity": "1"}
u["unicorn"] = {"name": "Unicorn", "dexterity": "2"}

v = {}
v["vampire"] = {}

v["vampire"]["regular"] = {"name": "Vampire", "dexterity": "4"}
v["vampire"]["spawn"] = {"name": "Vampire Spawn", "dexterity": "3"}

w = {}

w["water_weird"] = {"name": "R", "dexterity": "3"}
w["wight"] = {"name": "Wight", "dexterity": "2"}
w["will_o_wisp"] = {"name": "Will-o'-Wisp", "dexterity": "9"}
w["wraith"] = {"name": "Wraith", "dexterity": "3"}
w["wyvern"] = {"name": "Wyvern", "dexterity": "0"}

x = {}

x["xorn"] = {"name": "Xorn", "dexterity": "0"}

y = {}
y["yeti"] = {}
y["yuanti"] = {}
y["yugoloth"] = {}

y["yeti"]["regular"] = {"name": "Yeti", "dexterity": "1"}
y["yeti"]["abonimable"] = {"name": "Abominable Yeti", "dexterity": "0"}
y["yuanti"]["abomination"] = {"name": "Yuan-ti Abomination", "dexterity": "3"}
y["yuanti"]["malison"] = {"name": "Yuan-ti Malison", "dexterity": "2"}
y["yuanti"]["pureblood"] = {"name": "Yuan-ti Pureblood", "dexterity": "1"}
y["yugoloth"]["arcanaloth"] = {"name": "Arcanaloth", "dexterity": "1"}
y["yugoloth"]["mezzoloth"] = {"name": "Mezzoloth", "dexterity": "0"}
y["yugoloth"]["nycaloth"] = {"name": "Nycaloth", "dexterity": "0"}
y["yugoloth"]["ultroloth"] = {"name": "Ultroloth", "dexterity": "3"}

z = {}
z["zombie"] = {}

z["zombie"]["regular"] = {"name": "Zombie", "dexterity": "-2"}
z["zombie"]["ogre"] = {"name": "Ogre Zombie", "dexterity": "-2"}
z["zombie"]["beholder"] = {"name": "Beholder Zombie", "dexterity": "-1"}

misc_creatures = {}
misc_creatures["a"] = {}
misc_creatures["b"] = {}
misc_creatures["c"] = {}
misc_creatures["d"] = {}
misc_creatures["e"] = {}
misc_creatures["f"] = {}
misc_creatures["g"] = {}
misc_creatures["g"]["giant"] = {}
misc_creatures["h"] = {}
misc_creatures["i"] = {}
misc_creatures["j"] = {}
misc_creatures["k"] = {}
misc_creatures["l"] = {}
misc_creatures["m"] = {}
misc_creatures["n"] = {}
misc_creatures["o"] = {}
misc_creatures["p"] = {}
misc_creatures["q"] = {}
misc_creatures["r"] = {}
misc_creatures["s"] = {}
misc_creatures["s"]["swarm"] = {}
misc_creatures["t"] = {}
misc_creatures["u"] = {}
misc_creatures["v"] = {}
misc_creatures["w"] = {}
misc_creatures["x"] = {}
misc_creatures["y"] = {}
misc_creatures["z"] = {}

misc_creatures["a"]["ape"] = {"name": "Ape", "dexterity": "2"}
misc_creatures["a"]["awakened_shrub"] = {"name": "Awakened Shrub", "dexterity": "-1"}
misc_creatures["a"]["awakened_tree"] = {"name": "Awakened Tree", "dexterity": "-2"}
misc_creatures["a"]["axe_beak"] = {"name": "Axe Beak", "dexterity": "1"}
misc_creatures["b"]["baboon"] = {"name": "Baboon", "dexterity": "2"}
misc_creatures["b"]["badger"] = {"name": "Badger", "dexterity": "0"}
misc_creatures["b"]["bat"] = {"name": "Bat", "dexterity": "2"}
misc_creatures["b"]["black_bear"] = {"name": "Black Bear", "dexterity": "0"}
misc_creatures["b"]["blink_dog"] = {"name": "Blink Dog", "dexterity": "3"}
misc_creatures["b"]["blood_hawk"] = {"name": "Blood Hawk", "dexterity": "2"}
misc_creatures["b"]["boar"] = {"name": "Boar", "dexterity": "0"}
misc_creatures["b"]["brown_bear"] = {"name": "Brown Bear", "dexterity": "0"}
misc_creatures["c"]["camel"] = {"name": "Camel", "dexterity": "-1"}
misc_creatures["c"]["cat"] = {"name": "Cat", "dexterity": "2"}
misc_creatures["c"]["constrictor_snake"] = {"name": "Constrictor Snake", "dexterity": "2"}
misc_creatures["c"]["crab"] = {"name": "Crab", "dexterity": "0"}
misc_creatures["c"]["crocodile"] = {"name": "Crocodile", "dexterity": "0"}
misc_creatures["d"]["death_dog"] = {"name": "Death Dog", "dexterity": "2"}
misc_creatures["d"]["deer"] = {"name": "Deer", "dexterity": "3"}
misc_creatures["d"]["dire_wolf"] = {"name": "Dire Wolf", "dexterity": "2"}
misc_creatures["d"]["draft_horse"] = {"name": "Draft Horse", "dexterity": "0"}
misc_creatures["e"]["eagle"] = {"name": "Eagle", "dexterity": "2"}
misc_creatures["e"]["elephant"] = {"name": "Elephant", "dexterity": "-1"}
misc_creatures["e"]["elk"] = {"name": "Elk", "dexterity": "0"}
misc_creatures["f"]["flying_snake"] = {"name": "Flying Snake", "dexterity": "4"}
misc_creatures["f"]["frog"] = {"name": "Frog", "dexterity": "1"}
misc_creatures["g"]["giant"]["ape"] = {"name": "Giant Ape", "dexterity": "2"}
misc_creatures["g"]["giant"]["badger"] = {"name": "Giant Badger", "dexterity": "0"}
misc_creatures["g"]["giant"]["bat"] = {"name": "Giant Bat", "dexterity": "3"}
misc_creatures["g"]["giant"]["boar"] = {"name": "Giant Boar", "dexterity": "0"}
misc_creatures["g"]["giant"]["centipede"] = {"name": "Giant Centipede", "dexterity": "2"}
misc_creatures["g"]["giant"]["constrictor_snake"] = {"name": "Giant Constrictor Snake", "dexterity": "2"}
misc_creatures["g"]["giant"]["crab"] = {"name": "Giant Crab", "dexterity": "2"}
misc_creatures["g"]["giant"]["crocodile"] = {"name": "Giant Crocodile", "dexterity": "-1"}
misc_creatures["g"]["giant"]["eagle"] = {"name": "Giant Eagle", "dexterity": "3"}
misc_creatures["g"]["giant"]["elk"] = {"name": "Giant Elk", "dexterity": "3"}
misc_creatures["g"]["giant"]["fire_beetle"] = {"name": "Giant Fire Beetle", "dexterity": "0"}
misc_creatures["g"]["giant"]["goat"] = {"name": "Giant Goat", "dexterity": "0"}
misc_creatures["g"]["giant"]["hyena"] = {"name": "Giant Hyena", "dexterity": "2"}
misc_creatures["g"]["giant"]["lizard"] = {"name": "Giant Lizard", "dexterity": "1"}
misc_creatures["g"]["giant"]["octopus"] = {"name": "Giant Octopus", "dexterity": "1"}
misc_creatures["g"]["giant"]["owl"] = {"name": "Giant Owl", "dexterity": "2"}
misc_creatures["g"]["giant"]["poisonous_snake"] = {"name": "Giant Poisonous Snake", "dexterity": "4"}
misc_creatures["g"]["giant"]["rat"] = {"name": "Giant Rate", "dexterity": "2"}
misc_creatures["g"]["giant"]["scorpion"] = {"name": "Giant Scorpion", "dexterity": "1"}
misc_creatures["g"]["giant"]["sea_horse"] = {"name": "Giant Sea Horse", "dexterity": "2"}
misc_creatures["g"]["giant"]["shark"] = {"name": "Giant Shark", "dexterity": "0"}
misc_creatures["g"]["giant"]["spider"] = {"name": "Giant Spider", "dexterity": "3"}
misc_creatures["g"]["giant"]["toad"] = {"name": "Giant Toad", "dexterity": "1"}
misc_creatures["g"]["giant"]["vulture"] = {"name": "Giant Vulture", "dexterity": "0"}
misc_creatures["g"]["giant"]["wasp"] = {"name": "Giant Wasp", "dexterity": "2"}
misc_creatures["g"]["giant"]["weasel"] = {"name": "Giant Weasel", "dexterity": "3"}
misc_creatures["g"]["giant"]["wolf_spider"] = {"name": "Giant Wolf Spider", "dexterity": "3"}
misc_creatures["g"]["goat"] = {"name": "Goat", "dexterity": "0"}
misc_creatures["h"]["hawk"] = {"name": "Hawk", "dexterity": "3"}
misc_creatures["h"]["hunter_shark"] = {"name": "Hunter Shark", "dexterity": "1"}
misc_creatures["h"]["hyena"] = {"name": "Hyena", "dexterity": "1"}
misc_creatures["j"]["jackal"] = {"name": "Jackal", "dexterity": "2"}
misc_creatures["k"]["kiler_whale"] = {"name": "Killer Whale", "dexterity": "0"}
misc_creatures["l"]["lion"] = {"name": "Lion", "dexterity": "2"}
misc_creatures["l"]["lizard"] = {"name": "Lizard", "dexterity": "0"}
misc_creatures["m"]["mammoth"] = {"name": "Mammoth", "dexterity": "-1"}
misc_creatures["m"]["mastiff"] = {"name": "Mastiff", "dexterity": "2"}
misc_creatures["m"]["mule"] = {"name": "Mule", "dexterity": "0"}
misc_creatures["o"]["octopus"] = {"name": "Octopus", "dexterity": "2"}
misc_creatures["o"]["owl"] = {"name": "Owl", "dexterity": "1"}
misc_creatures["p"]["panther"] = {"name": "Panther", "dexterity": "2"}
misc_creatures["p"]["phase_spider"] = {"name": "Phase Spider", "dexterity": "2"}
misc_creatures["p"]["poisonous_snake"] = {"name": "Poisonous Snake", "dexterity": "3"}
misc_creatures["p"]["polar_bear"] = {"name": "Polar Bear", "dexterity": "0"}
misc_creatures["p"]["pony"] = {"name": "Pony", "dexterity": "0"}
misc_creatures["q"]["quipper"] = {"name": "Quipper", "dexterity": "3"}
misc_creatures["r"]["rat"] = {"name": "Rat", "dexterity": "0"}
misc_creatures["r"]["raven"] = {"name": "Raven", "dexterity": "2"}
misc_creatures["r"]["reef_shark"] = {"name": "Reef Shark", "dexterity": "1"}
misc_creatures["r"]["rhinoceros"] = {"name": "Rhinoceros", "dexterity": "-1"}
misc_creatures["r"]["riding_horse"] = {"name": "Riding Horse", "dexterity": "0"}
misc_creatures["s"]["sabertoothed_tiger"] = {"name": "Saber-Toothed Tiger", "dexterity": "2"}
misc_creatures["s"]["scorpion"] = {"name": "Scorpion", "dexterity": "0"}
misc_creatures["s"]["sea_horse"] = {"name": "Sea Horse", "dexterity": "1"}
misc_creatures["s"]["spider"] = {"name": "Spider", "dexterity": "2"}
misc_creatures["s"]["swarm"]["bats"] = {"name": "Swarm of Bats", "dexterity": "2"}
misc_creatures["s"]["swarm"]["insects"] = {"name": "Swarm of Insects", "dexterity": "1"}
misc_creatures["s"]["swarm"]["poisonous_snakes"] = {"name": "Swarm of Poisonous Snakes", "dexterity": "4"}
misc_creatures["s"]["swarm"]["quippers"] = {"name": "Swarm of Quippers", "dexterity": "3"}
misc_creatures["s"]["swarm"]["rats"] = {"name": "Swarm of Rats", "dexterity": "0"}
misc_creatures["s"]["swarm"]["ravens"] = {"name": "Swarm of Ravens", "dexterity": "2"}
misc_creatures["t"]["tiger"] = {"name": "Tiger", "dexterity": "2"}
misc_creatures["v"]["vulture"] = {"name": "Vulture", "dexterity": "0"}
misc_creatures["w"]["warhorse"] = {"name": "Warhorse", "dexterity": "1"}
misc_creatures["w"]["weasel"] = {"name": "Weasel", "dexterity": "3"}
misc_creatures["w"]["winter_wolf"] = {"name": "Winter Wolf", "dexterity": "1"}
misc_creatures["w"]["wolf"] = {"name": "Wolf", "dexterity": "2"}
misc_creatures["w"]["worg"] = {"name": "Worg", "dexterity": "1"}

npcs = {}

npcs["acolyte"] = {"name": "Acolyte", "dexterity": "0"}
npcs["archmage"] = {"name": "Archmage", "dexterity": "2"}
npcs["assassin"] = {"name": "Assassin", "dexterity": "3"}
npcs["bandit"] = {"name": "Bandit", "dexterity": "1"}
npcs["bandit_captain"] = {"name": "Bandit Captain", "dexterity": "3"}
npcs["commoner"] = {"name": "Commoner", "dexterity": "0"}
npcs["cultist"] = {"name": "Cultist", "dexterity": "1"}
npcs["cult_fanatic"] = {"name": "Cult Fanatic", "dexterity": "2"}
npcs["druid"] = {"name": "Druid", "dexterity": "1"}
npcs["gladiator"] = {"name": "Gladiator", "dexterity": "2"}
npcs["guard"] = {"name": "Guard", "dexterity": "1"}
npcs["knight"] = {"name": "Knight", "dexterity": "0"}
npcs["mage"] = {"name": "Mage", "dexterity": "2"}
npcs["noble"] = {"name": "Noble", "dexterity": "1"}
npcs["priest"] = {"name": "Priest", "dexterity": "0"}
npcs["scout"] = {"name": "Scout", "dexterity": "2"}
npcs["spy"] = {"name": "Spy", "dexterity": "2"}
npcs["thug"] = {"name": "Thug", "dexterity": "0"}
npcs["tribal_warrior"] = {"name": "Tribal Warrior", "dexterity": "0"}
npcs["veteran"] = {"name": "Veteran", "dexterity": "1"}

# Lost Mine of Phandelver
npcs["evil_mage"] = {"name": "Evil Mage", "dexterity": "2"}
npcs["mormesk_wraith"] = {"name": "Mormesk the Wraith", "dexterity": "3"}
npcs["nezznar"] = {"name": "Nezznar the Black Spider", "dexterity": "1"}
npcs["redbrand"] = {"name": "Redbrand Ruffian", "dexterity": "2"}
npcs["sildar"] = {"name": "Sildar Hallwinter", "dexterity": "0"}

# Homebrew
e["drow"]["wizard"] = {"name": "Drow Wizard", "dexterity": "2"}
d["devil"]["hellish_minotaur"] = {"name": "Hellish MInotaur", "dexterity": "0"}
n["neodorn"] = {"name": "Neodorn", "dexterity": "4"}
s["sharkan"] = {}
s["sharkan"]["flame"] = {}
s["sharkan"]["frost"] = {}
s["sharkan"]["storm"] = {}
s["sharkan"]["acid"] = {}
s["sharkan"]["flame"]["young"] = {"name": "Young Flame Sharkan", "dexterity": "1"}
s["sphinx"]["regular"] = {"name": "Sphinx", "dexterity": "2"}
npcs["kairon"] = {"name": "Kairon", "dexterity": "2"}


with open("a.json", "w") as file:
    json.dump(a, file, sort_keys=True, indent=2)
with open("b.json", "w") as file:
    json.dump(b, file, sort_keys=True, indent=2)
with open("c.json", "w") as file:
    json.dump(c, file, sort_keys=True, indent=2)
with open("d.json", "w") as file:
    json.dump(d, file, sort_keys=True, indent=2)
with open("e.json", "w") as file:
    json.dump(e, file, sort_keys=True, indent=2)
with open("f.json", "w") as file:
    json.dump(f, file, sort_keys=True, indent=2)
with open("g.json", "w") as file:
    json.dump(g, file, sort_keys=True, indent=2)
with open("h.json", "w") as file:
    json.dump(h, file, sort_keys=True, indent=2)
with open("i.json", "w") as file:
    json.dump(i, file, sort_keys=True, indent=2)
with open("j.json", "w") as file:
    json.dump(j, file, sort_keys=True, indent=2)
with open("k.json", "w") as file:
    json.dump(k, file, sort_keys=True, indent=2)
with open("l.json", "w") as file:
    json.dump(l, file, sort_keys=True, indent=2)
with open("m.json", "w") as file:
    json.dump(m, file, sort_keys=True, indent=2)
with open("n.json", "w") as file:
    json.dump(n, file, sort_keys=True, indent=2)
with open("o.json", "w") as file:
    json.dump(o, file, sort_keys=True, indent=2)
with open("p.json", "w") as file:
    json.dump(p, file, sort_keys=True, indent=2)
with open("q.json", "w") as file:
    json.dump(q, file, sort_keys=True, indent=2)
with open("r.json", "w") as file:
    json.dump(r, file, sort_keys=True, indent=2)
with open("s.json", "w") as file:
    json.dump(s, file, sort_keys=True, indent=2)
with open("t.json", "w") as file:
    json.dump(t, file, sort_keys=True, indent=2)
with open("u.json", "w") as file:
    json.dump(u, file, sort_keys=True, indent=2)
with open("v.json", "w") as file:
    json.dump(v, file, sort_keys=True, indent=2)
with open("w.json", "w") as file:
    json.dump(w, file, sort_keys=True, indent=2)
with open("x.json", "w") as file:
    json.dump(x, file, sort_keys=True, indent=2)
with open("y.json", "w") as file:
    json.dump(y, file, sort_keys=True, indent=2)
with open("z.json", "w") as file:
    json.dump(z, file, sort_keys=True, indent=2)
with open("misc_creatures.json", "w") as file:
    json.dump(misc_creatures, file, sort_keys=True, indent=2)
with open("npcs.json", "w") as file:
    json.dump(npcs, file, sort_keys=True, indent=2)
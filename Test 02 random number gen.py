fungi_violet_fungus = {}
fungi_violet_fungus ["name"] = "Violet Fungus"
fungi_violet_fungus ["dexterity"] = "-5"

# generate random floating point values
from random import seed
from random import randint
# seed random number generator
seed(randint(0, 100))

for _ in range(1):
	value = randint(1, 20) + int(fungi_violet_fungus["dexterity"])
	print("Test", value)


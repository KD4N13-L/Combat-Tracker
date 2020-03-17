fungi_violet_fungus = {}
fungi_violet_fungus ["name"] = "Violet Fungus"
fungi_violet_fungus ["dexterity"] = "-5"

# generate random floating point values
from random import seed
from random import randint
# seed random number generator
seed(randint(0, 100))
# generate random numbers between 0-1
for _ in range(20):
	value = randint(1, 20) + int(fungi_violet_fungus["dexterity"])
	print("Test", value)


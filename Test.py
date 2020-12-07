from Inventory_Tracker_classes import *

a = Shop()

print("Which store do you want to go to?: ")
print("Write 1 to go to the General Goods shop")
print("Write 2 to go to Gilmores Glorious Goods shop")
print("Write 3 to go to the Invulnerable Vagrant shop")
choice = input("Input your choice: ")

l = {"1": "general_shop", "2": "gilmores_glorious_goods", "3": "invulnerable_vagrant"}

for item in l.keys():
    if item == choice:
        a.importShop(l[item])

print("Welcome to our shop!")
print("Here is what we have available ~~~~~")
a.printStorage()
from Inventory_Tracker_classes import *


def Main():
    print("~~~~~~~ Welcome to the Inventory Tracker! ~~~~~~~")
    print("\n")
    print("Please create your character")
    print("\n")

    character_name = input("What is your name?: ")
    character_strength = input("On a scale of 1-20 how strong are you?: ")
    character_wealth = input("How many gold coins do you have?: ")

    character = Character(character_name, character_strength, character_wealth)
    shop_choice = Shop()

    while True:

        print("Which store do you want to go to?: ")
        print("Write 1 to go to the General Goods shop")
        print("Write 2 to go to Gilmores Glorious Goods shop")
        print("Write 3 to go to the Invulnerable Vagrant shop")
        choice = input("Input your choice: ")

        if choice == 1:
            shop_choice.importShop("general_shop")
        elif choice == 2:
            shop_choice.importShop("gilmores_glorious_goods")
        elif choice == 3:
            shop_choice.importShop("invulnerable_vagrant")

        print("Welcome to our shop!")
        print("Here is what we have available ~~~~~")
        shop_choice.printStorage()
        amount_of_items_you_wish_to_buy = int(input("How many items are you looking to buy from this store?: "))
        for i in range(amount_of_items_you_wish_to_buy):
            chosen_item = input("Please choose the item you wish to buy(case and spelling sensative): ")
            #shop_choice.getSpecificInformation(chosen_item)
            print("\n")
            keyboard = input("Do you wish to buy this item?(y/n): ")
            if keyboard == "y":
                character.addItem(chosen_item)
                print("Congratulations! May it serve you well!")

            else:
                print("I'll wait. Maybe you change your mind in the future.")
        break
    print("Thank you for using the Inventory tracker! Safe travels adventurer!!.")


Main()
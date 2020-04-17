import json
from random import randint
from random import seed


def npc_import():
    def update(updated_dictionary, dictionary_name):
        updated_dictionary.update({dictionary_name["name"]: randint(1, 20) + int(dictionary_name["dexterity"])})
        return updated_dictionary

    def dictionary_dig(dictionary):
        while 'name' not in dictionary.keys():
            hier = input("Input the creature's name. ---- ")
            dictionary = dictionary['' + hier + '']
        npcs_export = {}
        update(npcs_export, dictionary)
        return npcs_export

    seed(randint(1, 100))
    while True:
        npc_amount = input("How many NPCs are participating(0 to 15)? ---- ")
        if npc_amount == "0":
            blank_dictionary = {}
            return blank_dictionary
        else:
            for check in range(0, 15):
                if npc_amount == str(check):
                    npcs = int(npc_amount) + 1
                    if npcs <= 1:
                        pass
                    else:
                        final_npc_dictionary = {}
                        for variable_number in range(1, npcs):
                            name = input("Input the creature's alphabetical sorting letter. ---- ")
                            with open('' + name + '.json') as data_file:
                                data = json.load(data_file)
                            final_npc_dictionary.update(dictionary_dig(data))
                        return final_npc_dictionary
                    break
            print("Please insert a NON-negative INTEGER")


def pc_import():
    def pc_file_import():
        dictionary_name = input("What is the name of the Players File? ---- ")
        with open('' + dictionary_name + '.json') as data_file:
            dictionary = json.load(data_file)
        i_pc = 1
        updated_dictionary = {}
        while i_pc <= int(dictionary["amount"]):
            value_pc = 'player%d' % i_pc
            print(dictionary['' + value_pc + '']["name"])
            updated_dictionary.update({dictionary['' + value_pc + '']["name"]: int(input("Initiative Score: "))})
            i_pc += 1
        return updated_dictionary

    def pc_file_create():
        i_pc = 1
        dictionary_file_name = input("What would you like to name the new players file? ---- ")
        dictionary_destination = {"amount": int(input("How many PCs are participating? ---- "))}
        while i_pc <= dictionary_destination["amount"]:
            value_pc = 'player%d' % i_pc
            player = {}
            player[value_pc] = {"name": "blank", "initiative": 0, "dexterity": 0}
            print("Input information of PC", i_pc)
            player[value_pc].update({"name": input("Name: ")})
            player[value_pc].update({"initiative": 10})
            player[value_pc].update({"dexterity": int(input("Dexterity Modifier: "))})
            dictionary_destination.update({value_pc: player[value_pc]})
            i_pc += 1
        with open('' + dictionary_file_name + '.json', "w") as file:
            json.dump(dictionary_destination, file, indent=2)

        dictionary_name = dictionary_file_name
        with open('' + dictionary_name + '.json') as data_file:
            dictionary = json.load(data_file)
        i_pc = 1
        updated_dictionary = {}
        while i_pc <= int(dictionary["amount"]):
            value_pc = 'player%d' % i_pc
            print(dictionary['' + value_pc + '']["name"])
            updated_dictionary.update({dictionary['' + value_pc + '']["name"]: int(input("Initiative Score: "))})
            i_pc += 1
        return updated_dictionary

    choice = input("Would you like to use an ALREADY MADE set of PCs (Answer Yes/No)? ---- ")
    if choice == "Yes":
        updated_dictionary = pc_file_import()
        return updated_dictionary
    else:
        updated_dictionary = pc_file_create()
        return updated_dictionary


def initiative_display(dictionary):
    with open("initiative.json", "w") as file:
        json.dump(dictionary, file, sort_keys=True, indent=2)
    #    with open('' + dictionary + '.json', 'r') as file:
    #        initiative = json.load(file, sort_keys=True, indent=2)
    for key, value in sorted(dictionary.items(), key=lambda x: x[1], reverse=True):
        print(key, value)
    a = {}
    with open("initiative.json", 'w') as file1:
        json.dump(a, file1, sort_keys=True, indent=2)

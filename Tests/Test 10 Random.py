import json
from random import randint
from random import seed
seed(randint(1, 100))


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

npc_import()
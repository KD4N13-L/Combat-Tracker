import json

initiative = {}


def pc_import(dictionary_name):
    json_exten = ".json"
    name = str(dictionary_name) + json_exten
    with open('' + name + '') as data_file:
        dictionary = json.load(data_file)
    i_pc = 1
    dictionary_name["amount"] = dictionary["amount"]
    while i_pc <= dictionary_name["amount"]:
        value_pc = 'player%d' % i_pc
        player = {value_pc: {"name": "blank", "initiative": 0, "dexterity": 0}}
        print("Input information of PC", i_pc)
        player[value_pc]["name"] = dictionary["name"]
        print(player[value_pc]["name"])
        player[value_pc]["initiative"] = int(input("Initiative Score: "))
        player[value_pc]["dexterity"] = dictionary["dexterity"]
        initiative.update({player[value_pc]["name"]: player[value_pc]["initiative"]})
        i_pc += 1


def pc_create(dictionary_name):
    i_pc = 1
    dictionary_file_name = str(dictionary_name)
    dictionary_name = {"amount": int(input("How many PCs are participating? "))}
    while i_pc <= dictionary_name["amount"]:
        value_pc = 'player%d' % i_pc
        player = {value_pc: {"name": "blank", "initiative": 0, "dexterity": 0}}
        print("Input information of PC", i_pc)
        player[value_pc]["name"] = input("Name: ")
        player[value_pc]["initiative"] = int(input("Initiative Score: "))
        player[value_pc]["dexterity"] = int(input("Dexterity Modifier: "))
        initiative.update({player[value_pc]["name"]: player[value_pc]["initiative"]})
        # json_exten = ".json"
        # name = str(dictionary_name) + json_exten
        # file = open('' + name + '', "w")
        # file.write(json.dumps(dictionary_name))
        # file.close()

        json_exten = ".json"
        alph = str(dictionary_file_name) + json_exten
        # with open('' + alph + '', 'w') as file:
        #    json.dump(alph, file, sort_keys=True, indent=2)

        with open('' + alph + '', "w") as file:
            json.dump(dictionary_name, file, sort_keys=True, indent=2)

        i_pc += 1


dictionary_name = input("What is the name of the file you'd like to import? ")
pc_create(dictionary_name)

for key, value in sorted(initiative.items(), key=lambda x: x[1], reverse=True):
    print(key, value)

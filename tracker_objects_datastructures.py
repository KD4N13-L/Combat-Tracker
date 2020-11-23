import json
from random import randint
from random import seed
import os.path
from Final_Hashmap import *

seed(randint(1, 100))


def dict_dig_for_HashMap(dict_to_be_digged):
    hash_map = HashMap()
    for k, v in dict_to_be_digged.items():
        if type(v) == dict:
            v = dict_dig_for_HashMap(v)
        hash_map.put(k, v)
    return hash_map


def dict_to_hashmap(dict_to_be_transformed):
    hashmap = HashMap()
    for key, value in dict_to_be_transformed.items():
        final_value = value
        if type(value) == dict:
            final_value = dict_dig_for_HashMap(value)
        hashmap.put(key, final_value)
    return hashmap


class Participant:

    def __init__(self, name, modifier, initiative, player):
        self.name = name
        self.modifier = modifier
        self.initiative = initiative
        self.player = player
        self.extra_initiative = 0

    def display_participant(self):
        if self.modifier >= 0:
            new_mod = "+" + str(self.modifier)
            print(self.initiative, ":", self.name, "( Dexterity :", new_mod, ")")
        else:
            print(self.initiative, ":", self.name, "( Dexterity :", self.modifier, ")")


class Initiative:

    def __init__(self):
        self.creatures = []
        self.amount = 0

    def update(self, creature_list):
        sorting_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                           "s", "t", "u", "v", "w", "x", "y", "z", "misc", "npcs"]
        while True:
            alph_number = input("Input the creature's alphabetical sorting letter. ---- ")
            if alph_number in sorting_letters:
                with open('' + alph_number + '.json') as data_file:
                    dictionary = json.load(data_file)
                dictionary = dict_to_hashmap(dictionary)
                while not dictionary.hasKey('name'):
                    hier = input("Input the creature's name. ---- ")
                    while not dictionary.hasKey(hier):
                        hier = input("Such a creature doesn't exit. Try again. ---- ")
                    dictionary = dictionary.get('' + hier + '')
                name = dictionary.get("name")
                modifier = int(dictionary.get("dexterity"))
                initiative = randint(1, 20) + modifier
                player = False
                creature = Participant(name, modifier, initiative, player)
                creature_list.append(creature)
                print(creature.name, "has been added to the initiative!")
                return
            else:
                print("Such an alphabetical sorting letter doesn't exit.")

    def import_npcs(self, creature_amount):
        self.creatures.clear()
        creature_amount = int(creature_amount)
        while True:
            if creature_amount == 0:
                blank_list = []
                return blank_list
            else:
                for check in range(0, 15):
                    if creature_amount == check:
                        for i in range(0, creature_amount):
                            self.update(self.creatures)
                        return
                print("Please insert a NON-negative INTEGER from 0 to 15")

    def display_current_list(self):
        for creature in self.creatures:
            creature.display_participant()

    def import_char(self, participant):
        self.creatures.append(participant)
        print(participant.name, "has been added to the initiative!")
        self.amount += 1

    def sort_creatures(self):
        def initiative_sorter_score(participant):
            return participant.initiative

        def initiative_sorter_mod(participant):
            return participant.modifier

        def initiative_sorter_extra(participant):
            return participant.extra_initiative

        def roll_extra_initiative(participant):
            if participant.player:
                print(participant.name, "is tied on initiative with another participant. Ask "
                                        "them to roll initiative again.")
                participant.extra_initiative = int(input("Input the result. ---- "))
            else:
                participant.extra_initiative = randint(1, 20) + participant.modifier

        self.creatures.sort(key=initiative_sorter_score, reverse=True)
        check = Participant("name", 0, -10, False)
        for index1 in range(len(self.creatures) - 1):
            if self.creatures[index1].initiative != self.creatures[index1 + 1].initiative:
                pass
            elif check.initiative != self.creatures[index1].initiative:
                mini_list = [self.creatures[index1], self.creatures[index1 + 1]]
                check = self.creatures[index1]
                for index2 in range(index1 + 2, len(self.creatures)):
                    if self.creatures[index1].initiative == self.creatures[index2].initiative:
                        mini_list.append(self.creatures[index2])
                    else:
                        break
                mini_list.sort(key=initiative_sorter_mod, reverse=True)
                check2 = None
                for tempindex1 in range(len(mini_list) - 1):
                    if mini_list[tempindex1].modifier == mini_list[tempindex1 + 1].modifier and check2 != mini_list[tempindex1].modifier:
                        micro_list = [mini_list[tempindex1], mini_list[tempindex1 + 1]]
                        check2 = mini_list[tempindex1].modifier
                        for tempindex2 in range(tempindex1 + 2, len(mini_list)):
                            if mini_list[tempindex2].modifier == mini_list[tempindex1].modifier:
                                micro_list.append(mini_list[tempindex2])
                            else:
                                break
                        steps = 1
                        for creature in micro_list:
                            roll_extra_initiative(creature)
                            if steps > 1:
                                for i in range(len(micro_list) - 1):
                                    for j in (i + 1, len(micro_list) - 1):
                                        if micro_list[i].extra_initiative == micro_list[j].extra_initiative:
                                            roll_extra_initiative(creature)
                            steps += 1
                        micro_list.sort(key=initiative_sorter_extra, reverse=True)
                        step_index = 0
                        for i in mini_list:
                            if i.modifier == micro_list[0].modifier:
                                for x in micro_list:
                                    mini_list.pop(step_index)
                                    mini_list.insert(step_index, x)
                                    step_index += 1
                                break
                            else:
                                step_index += 1
                step_index = 0
                for i in self.creatures:
                    if i.initiative == mini_list[0].initiative:
                        for x in mini_list:
                            self.creatures.pop(step_index)
                            self.creatures.insert(step_index, x)
                            step_index += 1
                        break
                    else:
                        step_index += 1


class Player_list:

    def __init__(self):
        self.amount = 0
        self.participants = []

    def create_players(self, initiative_list):
        while True:
            try:
                amount = int(input("How many PCs are participating? ---- "))
                i_pc = 1
                dictionary_file_name = input("What would you like to name the new players file? ---- ")
                dictionary_destination = {"amount": amount}
                while i_pc <= amount:
                    value_pc = 'player%d' % i_pc
                    player = {value_pc: {"name": "blank", "initiative": 0, "dexterity": 0}}
                    print("Input information of PC", i_pc)
                    player[value_pc].update({"name": input("Name: ")})
                    player[value_pc].update({"initiative": 10})
                    player[value_pc].update({"dexterity": int(input("Dexterity Modifier: "))})
                    dictionary_destination.update({value_pc: player[value_pc]})
                    i_pc += 1
                with open('' + dictionary_file_name + '.json', "w") as file:
                    json.dump(dictionary_destination, file, indent=2)

                with open('' + dictionary_file_name + '.json') as data_file:
                    dictionary = json.load(data_file)
                dictionary = dict_to_hashmap(dictionary)
                i_pc = 1
                updated_list = []
                while i_pc <= int(dictionary.get("amount")):
                    value_pc = 'player%d' % i_pc
                    name = dictionary.get('' + value_pc + '').get("name")
                    modifier = dictionary.get('' + value_pc + '').get("dexterity")
                    print(name)
                    initiative = int(input("Initiative Score: "))
                    player = True
                    player = Participant(name, modifier, initiative, player)
                    updated_list.append(player)
                    self.participants += updated_list
                    i_pc += 1
                    updated_list = []
                initiative_list.creatures += self.participants
                return
            except ValueError:
                print("Please, enter an integer larger than 0.")

    def import_players(self, initiative_list):
        while True:
            dictionary_name = input("What is the name of the Players File you'd like to import? ---- ")
            dictionary_file = '' + dictionary_name + '.json'
            manager = os.path.isfile(dictionary_file)
            if manager:
                with open(dictionary_file) as data_file:
                    dictionary = json.load(data_file)
                dictionary = dict_to_hashmap(dictionary)
                i_pc = 1
                updated_list = []
                while i_pc <= int(dictionary.get("amount")):
                    value_pc = 'player%d' % i_pc
                    name = dictionary.get('' + value_pc + '').get("name")
                    modifier = dictionary.get('' + value_pc + '').get("dexterity")
                    print(name)
                    initiative = int(input("Initiative Score: "))
                    player = True
                    player = Participant(name, modifier, initiative, player)
                    updated_list.append(player)
                    self.participants += updated_list
                    i_pc += 1
                    updated_list = []
                initiative_list.creatures += self.participants
                return
            else:
                print("Such a Players File doesn't exit.")

# ----------------------------------------------------------------------------------------------------------

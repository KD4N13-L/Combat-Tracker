import json
from random import randint
from random import seed
import os.path
from Final_Hashmap import *
from deque_linked_list import *
from single_linked_list import *

seed(randint(1, 100))


class Participant:

    def __init__(self, name, modifier, initiative, player_boolean):
        self.name = name
        self.modifier = modifier
        self.initiative = initiative
        self.player_boolean = player_boolean
        self.extra_initiative = 0

    def display_participant(self):
        if self.modifier >= 0:
            new_mod = "+" + str(self.modifier)
            print(self.initiative, ":", self.name, "( Dexterity :", new_mod, ")")
        else:
            print(self.initiative, ":", self.name, "( Dexterity :", self.modifier, ")")


class Initiative:

    def __init__(self):
        self.creatures = SingleLinkedList()
        self.size = 0

    def update(self, creature_list):
        sorting_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                           "s", "t", "u", "v", "w", "x", "y", "z", "misc", "npcs"]
        while True:
            alph_number = input("Input the creature's alphabetical sorting letter (a-z, misc, npcs). ---- ")
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
                creature_list.insertLast(creature)
                print(creature.name, "has been added to the initiative!")
                return
            else:
                print("Such an alphabetical sorting letter doesn't exit.")

    def import_npcs(self, creature_amount):
        self.creatures.clear()
        creature_amount = int(creature_amount)
        while True:
            if creature_amount == 0:
                return
            else:
                for check in range(1, 15):
                    if creature_amount == check:
                        for i in range(0, creature_amount):
                            self.update(self.creatures)
                        return
                print("Please insert a NON-negative INTEGER from 0 to 15")

    def display_current_list(self):
        itr = self.creatures.first
        while itr:
            itr.data.display_participant()
            itr = itr.next

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

        _tbs_list = []
        itr = self.creatures.first
        while itr:
            _tbs_list.append(itr.data)
            itr = itr.next

        _tbs_list.sort(key=initiative_sorter_score, reverse=True)
        check = Participant("name", 0, -10, False)
        for index1 in range(len(_tbs_list) - 1):
            if _tbs_list[index1].initiative != _tbs_list[index1 + 1].initiative:
                pass
            elif check.initiative != _tbs_list[index1].initiative:
                mini_list = [_tbs_list[index1], _tbs_list[index1 + 1]]
                check = _tbs_list[index1]
                for index2 in range(index1 + 2, len(_tbs_list)):
                    if _tbs_list[index1].initiative == _tbs_list[index2].initiative:
                        mini_list.append(_tbs_list[index2])
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
                for i in _tbs_list:
                    if i.initiative == mini_list[0].initiative:
                        for x in mini_list:
                            _tbs_list.pop(step_index)
                            _tbs_list.insert(step_index, x)
                            step_index += 1
                        break
                    else:
                        step_index += 1
        self.creatures.clear()
        for i in _tbs_list:
            self.creatures.insertLast(i)


class Player_list:

    def __init__(self):
        self.amount = 0
        self.participants = LListDeque()

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

                dictionary = dict_to_hashmap(dictionary_destination)
                i_pc = 1
                while i_pc <= int(dictionary.get("amount")):
                    value_pc = 'player%d' % i_pc
                    name = dictionary.get('' + value_pc + '').get("name")
                    modifier = dictionary.get('' + value_pc + '').get("dexterity")
                    print(name)
                    initiative = int(input("Initiative Score: "))
                    player = True
                    player = Participant(name, modifier, initiative, player)
                    self.participants.insert_last(player)
                    i_pc += 1
                itr = self.participants.first
                while itr:
                    initiative_list.creatures.insertLast(itr.data)
                    initiative_list.size += 1
                    itr = itr.next
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
                while i_pc <= int(dictionary.get("amount")):
                    value_pc = 'player%d' % i_pc
                    name = dictionary.get('' + value_pc + '').get("name")
                    modifier = dictionary.get('' + value_pc + '').get("dexterity")
                    print(name)
                    initiative = int(input("Initiative Score: "))
                    player = True
                    player = Participant(name, modifier, initiative, player)
                    self.participants.insert_last(player)
                    i_pc += 1
                itr = self.participants.first
                while itr:
                    initiative_list.creatures.insertLast(itr.data)
                    initiative_list.size += 1
                    itr = itr.next
                return
            else:
                print("Such a Players File doesn't exit.")

# ----------------------------------------------------------------------------------------------------------

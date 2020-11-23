from random import randint
from random import seed

seed(randint(1, 100))


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
            print(self.initiative, ":", self.name, "( Modifier :", new_mod, ")")
        else:
            print(self.initiative, ":", self.name, "( Modifier :", self.modifier, ")")




def sort_creatures(self):
    def initiative_sorter_score(participant):
        return participant.initiative

    def initiative_sorter_mod(participant):
        return participant.modifier

    def initiative_sorter_extra(participant):
        return participant.extra_initiative

    self.sort(key=initiative_sorter_score, reverse=True)
    check = Participant("name", 0, -10, False)
    for index1 in range(len(self) - 1):
        print(self[index1])
        print(self[index1].initiative)
        if self[index1].initiative != self[index1 + 1].initiative:
            pass
        elif check.initiative != self[index1].initiative:
            mini_list = [self[index1], self[index1 + 1]]
            check = self[index1]
            for index2 in range(index1 + 2, len(self)):
                if self[index1].initiative == self[index2].initiative:
                    mini_list.append(self[index2])
                else:
                    break

            mini_list.sort(key=initiative_sorter_mod, reverse=True)

            # mini_list - same initiative score

            print("Mini List:")
            for i in mini_list:
                i.display_participant()
            print()
            check2 = None
            for tempindex1 in range(len(mini_list) - 1):
                if mini_list[tempindex1].modifier == mini_list[tempindex1 + 1].modifier and check2 != mini_list[tempindex1].modifier:
                    micro_list = [mini_list[tempindex1], mini_list[tempindex1 + 1]]
                    check2 = mini_list[tempindex1].modifier

                    # micro_list - mini_list + same modifier score

                    for tempindex2 in range(tempindex1 + 2, len(mini_list)):
                        if mini_list[tempindex2].modifier == mini_list[tempindex1].modifier:
                            micro_list.append(mini_list[tempindex2])
                        else:
                            break
                    for item_index in micro_list:
                        if item_index.player:
                            print(item_index.name, "is tied on initiative with another participant. Ask "
                                                   "them to roll initiative again.")
                            item_index.extra_initiative = int(input("Input the result. ---- "))
                        else:
                            item_index.extra_initiative = randint(1, 20) + item_index.modifier
                            print("Oni Extra Initiative")
                            print(item_index.extra_initiative)

                    micro_list.sort(key=initiative_sorter_extra, reverse=True)

                    print("Micro List")
                    for i in micro_list:
                        i.display_participant()
                    print()

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

                    print("Mini List")
                    for i in mini_list:
                        i.display_participant()
                    print()

            step_index = 0
            for i in self:
                if i.initiative == mini_list[0].initiative:
                    for x in mini_list:
                        self.pop(step_index)
                        self.insert(step_index, x)
                        step_index += 1
                    break
                else:
                    step_index += 1
    return self


list1 = []
part1 = Participant("Garry", -1, 12, True)
part2 = Participant("Matt", 1, 12, True)
part3 = Participant("Oni", 1, 12, False)
part4 = Participant("Kyle", 1, 12, True)

list1.append(part1)
list1.append(part2)
list1.append(part3)
list1.append(part4)

sort_creatures(list1)

print("Final Initiative")
for creature in list1:
    creature.display_participant()

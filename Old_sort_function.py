self.creatures.sort(key=initiative_sorter, reverse=True)
        list_length = len(self.creatures)
        for index1 in range(list_length - 1):
            index2 = index1 + 1
            if self.creatures[index1].initiative == self.creatures[index2].initiative:
                if self.creatures[index1].modifier < self.creatures[index2].modifier:
                    temp = self.creatures[index1]
                    self.creatures[index1] = self.creatures[index2]
                    self.creatures[index2] = temp
                elif self.creatures[index1].modifier == self.creatures[index2].modifier:
                    if self.creatures[index1].player:
                        print(self.creatures[index1].name, "is tied on initiative with another participant. Ask them "
                                                           "to roll initiative again.")
                        initiative1 = int(input("Input the reult. ---- "))
                    else:
                        initiative1 = randint(1, 20) + self.creatures[index1].modifier
                    if self.creatures[index2].player:
                        print(self.creatures[index2].name, "is tied on initiative with another participant. Ask them "
                                                           "to roll initiative again.")
                        initiative2 = int(input("Input the reult. ---- "))
                    else:
                        initiative2 = randint(1, 20) + self.creatures[index2].modifier
                    if initiative1 < initiative2:
                        temp = self.creatures[index1]
                        self.creatures[index1] = self.creatures[index2]
                        self.creatures[index2] = temp
        return self.creatures
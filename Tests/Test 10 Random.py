list1 = [1, 2, 2, 3, 4, 5]
list2 = [2, 4]
#for i in list1:
 #   if i == list2:
  #      index = list1.index(i)
   #     list1.remove(i)

#print(list1)

list3 = [6, 7, 8]

#for x in list3:
 #   list1.insert(index, x)
  #  index += 1

#print(list1)


def Diff(li1, li2):
    return (list(set(li1) - set(li2)))

print(Diff(list1, list2))

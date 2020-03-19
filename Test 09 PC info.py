import json
initiative = {}

#First time, for creating the json file wit PC information
players_group_A={}
i = 1
pcs = int(input("How many PCs are participating? "))
players_group_A["amount"] = pcs
while i<=pcs:
    value = 'player%d' % i
    players_group_A[value] = {"name": "blank", "initiative": 0, "dexterity": 0}
    print("Input information of PC", i)
    players_group_A[value]["name"] = input("Name: ")
    players_group_A[value]["initiative"] = int(input("Initiative Score: "))
    players_group_A[value]["dexterity"] = int(input("Dexterity Modifier: "))
    initiative.update({players_group_A[value]["name"]: players_group_A[value]["initiative"]})
    file = open("players_group_A.json", "w")
    file.write(json.dumps(players_group_A))
    file.close()
    i += 1


#Next time, for reusing already set PC information
players_group_A={}
i = 1
with open("players_group_A.json") as data_file:
    players_group_A = json.load(data_file)
while i<=int(players_group_A["amount"]):
    value = 'player%d' % i
    print("Input information of PC", i)
    print(players_group_A[value]["name"])
    players_group_A[value]["initiative"] = int(input("Initiative Score: "))
    initiative.update({players_group_A[value]["name"]: players_group_A[value]["initiative"]})
    i += 1

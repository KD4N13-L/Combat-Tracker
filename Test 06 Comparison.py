aarakocra = {}
aarakocra ["name"] = "Aarakocra"
aarakocra ["dexterity"] = "2"

aboleth = {}
aboleth ["name"] = "Aboleth"
aboleth ["dexterity"] = "-1"

devil_erinyes = {}
devil_erinyes ["name"] = "Erinyes"
devil_erinyes ["dexterity"] = "3"

d = {aarakocra ["name"]: int(aarakocra["dexterity"]), aboleth ["name"]: int(aboleth["dexterity"]), devil_erinyes ["name"]: int(devil_erinyes ["dexterity"])}

a = sorted(d.items(), key=lambda x:x[1], reverse=True)

print(a)
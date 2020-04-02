import json

personal_budget = {}
personal_budget ["date"] = "26.02.2020"

# Not the first time using the app, with already inserted data
with open("personal_budget.json") as data_file:
    personal_budget_saved = json.load(data_file)

print("You have old data", personal_budget_saved)
reuse = input("DO you want to use the data? Please answer Yes or No ")
if reuse == "Yes":
    personal_budget["wallet"] = personal_budget_saved["wallet"]
    personal_budget["income"] = personal_budget_saved["income"]
else:
    wallet = int(input("Insert te amount of money currently in your wallet "))

    personal_budget ["wallet"] = wallet

    print ("You will be asked to insert your predicted income for this month")

    personal_budget["parent_reg"] = int(input("How much money are you expecting to get from your parents this month? "))
    # Make the question more clear
    personal_budget["job"] = int(input("How much money will you get from your job/internship/etc.? "))
    personal_budget["other_inc"] = int(input("How much money will you get from other sources? "))

print("Your current data looks like this", personal_budget)
save = input("Do you want to save the income data? Please say Yes or No ")
if save == "Yes":
    file = open("personal_budget.json", "w")
    file.write(json.dumps(personal_budget))
    file.close()
else:
    print ("your answer was ", save)
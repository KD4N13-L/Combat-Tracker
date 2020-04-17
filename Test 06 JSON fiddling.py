import json

x_name = "x"
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

with open (''+x_name+'.json', 'w') as file:
    json.dump(x, file, indent=2)

z = json.dumps(x, indent=2)

y = {
    "year": "1985"
}

with open(''+x_name+'.json') as file1:
    json.load()

z.update(y, indent=2)
print(z)
dict = {
    "1": "1",
    "name": "ABCD"
}

for key, value in sorted(dict.items(), key=lambda x: x[1], reverse=True):
    print(key, value)

#letters first then numbers
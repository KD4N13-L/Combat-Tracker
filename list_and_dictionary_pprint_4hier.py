import json


def import_dictionary(dictionary_name):
    json_exten = ".json"
    alph = str(dictionary_name) + json_exten
    with open('' + alph + '') as file_data:
        dictionary_name = json.load(file_data)

    return dictionary_name


def display_dict_value(current_value, step=0):
    if type(current_value) == list:
        for item in current_value:
            display_dict_value(item, step + 1)
            print(", ", end="")
        print("\n", end="")

    elif type(current_value) == dict:
        for key in current_value:
            print("\n", "\t" * step, key, ": ", end="")
            display_dict_value(current_value[key], step + 1)
    else:
        print(current_value, end="")


def main():
    import_dictionary(input("Please insert the dictionary name: "))
    dictionary_name = import_dictionary(input("Please insert the dictionary name: "))
    display_dict_value(dictionary_name)


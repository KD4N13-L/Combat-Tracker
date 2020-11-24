from Final_Hashmap import *
from tracker_objects_datastructures import *

dictionary_name = input("What is the name of the Players File you'd like to import? ---- ")
dictionary_file = '' + dictionary_name + '.json'
with open(dictionary_file) as data_file:
    dictionary = json.load(data_file)
dictionary = dict_to_hashmap(dictionary)

dictionary.nested_print()


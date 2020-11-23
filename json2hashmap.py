import json
from Final_Hashmap import *


def dict_dig_for_HashMap(dict_to_be_digged):
    hash_map = HashMap()
    for k, v in dict_to_be_digged.items():
        if type(v) == dict:
            v = dict_dig_for_HashMap(v)
        hash_map.put(k, v)
    return hash_map


def dict_to_hashmap(dict_to_be_transformed):
    with open('' + dict_to_be_transformed + '.json') as data_file:
        dictionary = json.load(data_file)
    hashmap = HashMap()
    for key, value in dictionary.items():
        final_value = value
        if type(value) == dict:
            final_value = dict_dig_for_HashMap(value)
        hashmap.put(key, final_value)
    return hashmap



# FINISHED

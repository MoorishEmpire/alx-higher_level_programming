#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    key = next(iter(a_dictionary), None)
    max = next(iter(a_dictionary.values()), None)
    for item in a_dictionary:
        if a_dictionary[item] > max:
            max = a_dictionary[item]
            key = item
    return key

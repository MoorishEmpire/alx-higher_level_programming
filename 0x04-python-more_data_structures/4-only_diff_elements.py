#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result_set = set()
    for item in set_1:
        if item not in set_2:
            result_set.add(item)
    for item in set_2:
        if item not in set_1:
            result_set.add(item)
    return result_set

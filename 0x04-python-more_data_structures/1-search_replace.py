#!/usr/bin/python3
def search_replace(my_list, search, replace):
    size = len(my_list)
    if size == 0:
        return []
    new_list = [0] * size
    for i in range(0, size):
        if (my_list[i] == search):
            new_list[i] = replace
        else:
            new_list[i] = my_list[i]
    return new_list

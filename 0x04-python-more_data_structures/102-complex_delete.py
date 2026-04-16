#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    my_list = []
    for item in a_dictionary:
        if (a_dictionary[item] == value):
            my_list.append(item)
    for i in range(len(my_list)):
        del a_dictionary[my_list[i]]
    return a_dictionary

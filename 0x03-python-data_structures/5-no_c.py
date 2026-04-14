#!/usr/bin/python3
def no_c(my_string):
    if (len(my_string) == 0):
        return None
    my_string = my_string.replace("c", "")
    my_string = my_string.replace("C", "")
    return (my_string)

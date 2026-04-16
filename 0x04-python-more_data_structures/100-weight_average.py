#!/usr/bin/python3
def weight_average(my_list=[]):
    if (len(my_list) == 0):
        return 0
    tmp = 0
    div = 0
    for item in my_list:
        a, b = item
        tmp += a * b
        div += b
    return float(tmp / div)

def safe_print_list(my_list=[], x=0):
    i = 0
    for item in my_list:
        if (i < x):
            print(my_list[i], end="")
            i += 1
    print()
    return i

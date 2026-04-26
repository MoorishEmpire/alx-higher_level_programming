#!/usr/bin/python3
"""Module that contains the append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a new_tring to filename after each line containing a search_string
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            if search_string in line:
                file.write(line + new_string)
            else:
                file.write(line)

#!/usr/bin/python3
"""Module that contains the append_write function"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of text file
    and returns the number of characters added
    """
    with open(filename, "a") as file:
        return file.write(text)

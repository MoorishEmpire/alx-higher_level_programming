#!/usr/bin/python3
"""Module contains the write_file definition"""


def write_file(filename="", text=""):
    """
    Write a string to a text file and returns the number of characters written
    """
    with open(filename, "w") as file:
        return file.write(text)

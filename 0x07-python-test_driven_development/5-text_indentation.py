#!/usr/bin/python3
"""
Print a text with 2 new lines after each of these characters: ., ? and :

This module provide the text_indentation function.
"""


def text_indentation(text):
    """
    Print the text with 2 new lines after line.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    line = ""
    for item in text:
        if item not in [".", "?", ":"]:
            line += item
        else:
            print(f"{line.strip()}{item}")
            print()
            line = ""
    if len(line) > 0:
        print(f"{line.strip()}", end="")

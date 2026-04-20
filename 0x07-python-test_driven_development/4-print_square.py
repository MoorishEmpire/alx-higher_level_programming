#!/usr/bin/python3
"""
Prints a square with the character #.

This module provide the print_square function.
"""


def print_square(size):
    """
    Prints a square with it's size is size.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    else:
        if size < 0:
            raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
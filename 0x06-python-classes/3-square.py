#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Initialize a new Square with a given size with a validation check."""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = int(size)

    """ Return the cuurent square area"""
    def area(self):
        return self.__size ** 2

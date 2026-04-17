#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Initialize a new Square with a given size."""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = int(size)

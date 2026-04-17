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

    """ Getter for the private instance attribute size."""
    @property
    def size(self):
        return self.__size

    """ Setter for the private instance attribute size."""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ Return the cuurent square area"""
    def area(self):
        return self.__size ** 2

    """ Print in stdout the Square instance object with chr #"""
    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("#" * self.__size)

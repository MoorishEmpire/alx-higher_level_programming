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

    """ Checks if the self object square is equal to other object square. """
    def __eq__(self, other):
        if Square.area(self) == Square.area(other):
            return True
        return False

    """Checks if the self object square is not equal to other object square"""
    def __ne__(self, other):
        if Square.area(self) != Square.area(other):
            return True
        return False

    """Checks if the self object square is greater then other object square"""
    def __gt__(self, other):
        if Square.area(self) > Square.area(other):
            return True
        return False

    """Compare if self square area is greater or equal to other square area"""
    def __ge__(self, other):
        if Square.area(self) >= Square.area(other):
            return True
        return False

    """ Checks if the self  object square is lower then other object square."""
    def __lt__(self, other):
        if Square.area(self) < Square.area(other):
            return True
        return False

    """Compares if self square are is lower or equal to other square area"""
    def __le__(self, other):
        if Square.area(self) <= Square.area(other):
            return True
        return False

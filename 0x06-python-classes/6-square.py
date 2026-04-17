#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Initialize a new Square with a given size with a validation check."""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (not isinstance(position, tuple) or len(position) != 2 or
                not isinstance(position[0], int) or
                not isinstance(position[1], int) or
                position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = int(size)
        self.__position = position

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

    """ Getter for the private instance attribute position."""
    @property
    def position(self):
        return self.__position

    """ Setter for the private instance attribute position. """
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """ Return the cuurent square area"""
    def area(self):
        return self.__size ** 2

    """ Print in stdout the Square instance object with chr #"""
    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

#!/usr/bin/python3
"""Module that contains Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return super().area()

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"

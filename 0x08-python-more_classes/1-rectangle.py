#!/usr/bin/python3
"""Module define a Rectangle classe that define a rectangle"""


class Rectangle:
    """Define a rectangle"""

    """intializer for the new object created"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    """Geter for the private instance attribute width"""
    @property
    def width(self):
        return self.__width

    """Seter for the private instance attribute width"""
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """Geter for the private instance attribute height"""
    @property
    def height(self):
        return self.__height

    """Setter for the private instance attribute height"""
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

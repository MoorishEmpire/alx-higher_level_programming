#!/usr/bin/python3
"""Module that contains BaseGeometry class"""


class BaseGeometry:
    """Class"""

    def area(self):
        """Raises an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer greater than 0."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


"""
Module that contains rectangle class that inherites from BaseGeometry class
"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

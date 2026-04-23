#!/usr/bin/python3
"""Module that contains an empty calss"""


class BaseGeometry:
    """Class"""

    """Raises an Exception message"""
    def area(self):
        raise Exception("area() is not implemented")

    """Validated value if not int or les or equal ot 0 raise an Error"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

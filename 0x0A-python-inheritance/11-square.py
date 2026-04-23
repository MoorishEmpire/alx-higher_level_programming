#!/usr/bin/python3
"""Module that contains Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        super().__init__(size, size)
    
    def area(self):
        return super().area()

    def __str__(self):
        return super().__str__()

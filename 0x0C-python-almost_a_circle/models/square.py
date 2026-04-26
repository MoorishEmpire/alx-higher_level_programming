#!/usr/bin/python3
"""
Module that contains the class Sqaure
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Rectangle that inherits from class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a pritable format string of Square instance"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

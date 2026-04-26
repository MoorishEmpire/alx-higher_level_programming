#!/usr/bin/python3
"""
Module that contains the class Sqaure
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Rectangle that inherits from class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

    def __str__(self):
        """Returns a pritable format string of Square instance"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute if args exist and is not empty
        if yes Assigns a key/value argument to attributes
        """

        if len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.x = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

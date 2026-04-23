#!/usr/bin/python3
"""Module contains the Student class"""


class Student():
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs and all(isinstance(attr, str) for attr in attrs):
            dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    dict[attr] = getattr(self, attr)
            return dict
        return self.__dict__

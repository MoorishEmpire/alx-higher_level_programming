#!/usr/bin/python3
"""
Module That contains the Base class
"""
import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method
        Return the JSON string representation of list_dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file
        named of obj class_name + ".json" if list_objs is not None
        if is None writes an empty list
        """

        file_name = cls.__name__ + ".json"
        if list_objs is None:
            with open(file_name, "w") as file:
                json.dump([], file)
            return
        with open(file_name, "w") as file:
            json.dump([obj.to_dictionary() for obj in list_objs], file)

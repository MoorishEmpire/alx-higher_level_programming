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
        if list_objs is None or len(list_objs) == 0:
            json_str = cls.to_json_string(None)
        else:
            dicts = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(dicts)
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(json_str)

    def from_json_string(json_string):
        """
        Return the list of JSON string representation of json_string
        Or empty list if json_string is None or empty
        """

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)
        else:
            obj = cls()
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances retrived from the file <class name>.json
        or an empty list if the file deosn't exit
        """

        if cls.__name__ == "Rectangle":
            try:
                with open("Rectangle.json", "r") as f:
                    raw = f.read()

                dicts = cls.from_json_string(raw)
                lst = [None] * len(dicts)
                for i, d in enumerate(dicts):
                    lst[i] = cls.create(**d)
                return lst

            except FileNotFoundError:
                return []
        elif cls.__name__ == "Square":
            try:
                with open("Square.json", "r") as f:
                    raw = f.read()
                dicts = cls.from_json_string(raw)
                lst = [None] * len(dicts)
                for i, d in enumerate(dicts):
                    lst[i] = cls.create(**d)
                return lst

            except FileNotFoundError:
                return []

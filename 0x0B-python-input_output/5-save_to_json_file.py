#!/usr/bin/python3
"""Modules that define save_to_json function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using JSON representation"""
    with open(filename, "w") as file:
        if isinstance(my_obj, dict):
            json.dump(my_obj, file)
            return
        json.dump(my_obj, file)

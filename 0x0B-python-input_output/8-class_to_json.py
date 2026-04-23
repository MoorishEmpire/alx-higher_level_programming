#!/usr/bin/python3
"""Module contains the class class_to_json"""


def class_to_json(obj):
    """Returns the dictionary description with simple data stucture"""
    return obj.__dict__

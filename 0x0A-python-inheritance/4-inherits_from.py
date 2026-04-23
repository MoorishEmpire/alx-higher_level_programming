#!/usr/bin/python3
"""Module that defines the fucntion inherits_from"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of the class that
    inherited form otherwise returns False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

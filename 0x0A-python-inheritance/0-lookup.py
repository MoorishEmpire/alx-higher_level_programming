#!/usr/bin/python3
"""
Returns the list of available attributes and methods of an object.
"""


def lookup(obj):
    """Return a sorted list of all valid attributes and methods of obj.
    """
    return dir(obj)

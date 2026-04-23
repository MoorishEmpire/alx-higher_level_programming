#!/usr/bin/python3
"""Module that defines the fucntion is_same_class"""


def is_same_class(obj, a_class):
    """Returns True if obj is exactlyy an instance of the a_class class
    otherwise returns False
    """
    if type(obj) is a_class:
        return True
    return False

#!/usr/bin/python3
"""Module that defines the fucntion is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of the a_class class
    or an istance of a class that inheited from
    otherwise returns False
    """
    if isinstance(obj, a_class):
        return True
    return False

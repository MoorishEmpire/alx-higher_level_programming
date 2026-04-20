#!/usr/bin/python3
"""
Prints full name.

This module provides the say_my_name function.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first_name> <last_name>.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if not last_name:
        print(f"My name is {first_name}")
    else:
        print(f"My name is {first_name} {last_name}")

#!/usr/bin/python3
"""Modules that defines a LockedCalss class"""


class LockedClass:
    """
    Prevents the user for dynamically creating new instance attributes.
    """
    __slots__ = ["first_name"]

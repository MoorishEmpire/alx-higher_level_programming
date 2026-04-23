#!/usr/bin/python3
"""Module contains the Mylist class"""


class MyList(list):
    """Class inherets form list class prints a sorted list
    with using the print_sorted instance method.
    """
    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))

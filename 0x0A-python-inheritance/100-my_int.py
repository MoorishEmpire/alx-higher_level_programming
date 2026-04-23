#!/usr/bin/python3
"""Module that contains the class MyInt"""


class MyInt(int):
    """Class that inheretes from int class but invertes the == and != """
    def __init__(self, integer):
        self.__integer = integer

    def __eq__(self, other):
        return self.__integer != other

    def __ne__(self, other):
        return self.__integer == other

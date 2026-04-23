#!/usr/bin/python3
"""Module contains the read_file deffinition"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout"""
    with open(filename, "r") as file:
        print(file.read())

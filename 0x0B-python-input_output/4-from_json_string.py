#!/usr/bin/python3
"""Module that containes from_json_string function"""
import json


def from_json_string(my_str):
    """Returns a Python data structure represented by a Json string"""

    return json.loads(my_str)

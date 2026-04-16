#!/usr/bin/python3
import os


def safe_function(fct, *args):
    try:
        return fct(*args)
    except IndexError:
        os.write(2, b"Exception: list index out of range\n")
        return None
    except ZeroDivisionError:
        os.write(2, b"Excpetion: division by zero\n")
        return None

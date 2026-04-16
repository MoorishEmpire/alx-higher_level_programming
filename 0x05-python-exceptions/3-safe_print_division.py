#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = float(a / b)
        return div
    except ZeroDivisionError:
        return None
    finally:
        if (b == 0):
            print("Inside result:", None)
        else:
            print("Inside results: ", div)

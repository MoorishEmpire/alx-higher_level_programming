#!/usr/bin/python3
from calculator_1 import add
from calculator_1 import sub
from calculator_1 import div
from calculator_1 import mul
import sys
if __name__ == "__main__":
    argc = len(sys.argv) - 1
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    if (argc < 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print("1")
        exit(1)
    if (op == '+'):
        print("{} + {} = {}".format(a, b, add(a, b)))
        print("0")
    elif (op == '*'):
        print("{} * {} = {}".format(a, b, mul(a, b)))
        print("0")
    elif (op == '-'):
        print("{} {} {}".format(a, b, sub(a, b)))
        print("0")
    elif (op == '/'):
        print("{} / {} = {}".format(a, b, div(a, b)))
        print("0")
    else:
        print("unknown operator. Available operators: +, -, * and /")
        exit(1)

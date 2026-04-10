#!/usr/bin/python3
islower = __import__('7-islower').islower
def uppercase(str):
    for c in str:
        if(islower(c)):
            print(chr(ord(c) - 32), end="")
        else:
            print(c, end="")
    print("")

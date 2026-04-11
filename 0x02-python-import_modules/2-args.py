#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv) - 1
    if (argc == 1):
        print(argc, "argument:")
    elif (argc > 1):
        print(argc, "arguments:")
    else:
        print(argc, "arguments.")
    if (argc > 0):
        for i in range(1, argc + 1):
            print("{}: {}".format(i, sys.argv[i]))

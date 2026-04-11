#!/usr/bin/python3
import sys
argc = len(sys.argv) - 1
if (argc == 1):
    print(argc, "argument:")
elif (argc > 1):
    print(argc, "arguments:")
else:
    print(argc, "arguments.")
for i in range(1, argc + 1):
    print("{}: {}".format(i, sys.argv[i]))

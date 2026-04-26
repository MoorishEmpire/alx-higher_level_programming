#!/usr/bin/python3
"""
Module that contains a program that reads line by line and computes metrics
"""


def main():
    """main function"""
    dict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    file_size = 0
    nb_line = 0
    try:
        while True:
            line = input().split()
            status = int(line[-2])
            size = int(line[-1])
            if status in dict:
                file_size += size
                dict[status] += 1
                nb_line += 1
            if nb_line == 10:
                print(f"File size: {file_size}")
                for key in dict:
                    if dict[key] != 0:
                        print(f"{key}: {dict[key]}")
                nb_line = 0
    except (KeyboardInterrupt, EOFError):
        print(f"File size: {file_size}")
        for key in dict:
            if dict[key] != 0:
                print(f"{key}: {dict[key]}")


if __name__ == "__main__":
    main()

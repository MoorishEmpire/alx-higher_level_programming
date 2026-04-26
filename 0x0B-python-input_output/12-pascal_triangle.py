#!/usr/bin/
"""Module contains the pascal_triangle function"""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing the Pascal's triangle of n
    """
    if n <= 0:
        return [[]]
    new = [[1] * i for i in range(1, n + 1)]

    i = 0
    for row in new:
        for j in range(1, len(row)):
            if j <= i - 1:
                new[i][j] = new[i - 1][j - 1] + new[i - 1][j]
        i += 1
    return new

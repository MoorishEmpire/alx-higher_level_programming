#!/usr/bin/python3
"""
Divides all elements of matrix.

This modules returns the new_matrix with all elements divide.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of matrix and returns a new_matrix.
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    size = len(matrix[0])
    new_matrix = [[0] * len(matrix[0]) for i in range(len(matrix))]
    i = 0
    for row in matrix:
        if size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        j = 0
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            new_matrix[i][j] = round(item / div, 2)
            j += 1
        i += 1

    return new_matrix

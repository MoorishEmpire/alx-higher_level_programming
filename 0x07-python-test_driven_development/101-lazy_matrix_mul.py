#!/usr/bin/python3
"""
Return a new_matrice the result of 2 matrices multiplication.

Module provide the matrices multiplication function.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function return a new_matrice the result of m_a and m_b multiplication.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")

    size_a = len(m_a[0])

    for row in m_a:
        if size_a != len(row):
            raise TypeError("each row of m_a must be of the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    size_b = len(m_b[0])

    for row in m_b:
        if size_b != len(row):
            raise TypeError("each row of m_b must be of the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    if size_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(m_a, m_b)

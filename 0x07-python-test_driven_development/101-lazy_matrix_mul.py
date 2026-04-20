#!/usr/bin/python3
import numpy as np
"""
Return a new_matrice the result of 2 matrices multiplication.

Module provide the matrices multiplication function.
"""


def lazy_matrix_mul(m_a, m_b):
    """
    Function return a new_matrice the result of m_a and m_b multiplication.
    """
    m_a = np.array(m_a)
    m_b = np.array(m_b)

    return m_a @ m_b

#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")

    size_a = len(m_a[0])

    
    for row in m_a:
        if size_a != len(row):
            raise TypeError("each row of m_a must be the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("m_a should contain only integers or floats")


    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    size_b = len(m_b[0])

    for row in m_b:
        if size_b != len(row):
            raise TypeError("each row of m_b must be the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    return ([[sum(a_item * b_item for a_item, b_item in zip(A_row, B_col))
            for B_col in zip(*m_b)]
            for A_row in m_a])

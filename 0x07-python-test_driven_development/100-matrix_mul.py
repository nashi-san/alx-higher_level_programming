#!/usr/bin/python3

"""
multiply matrices module
this module contains a function that multiply matrices

"""


def matrix_mul(m_a, m_b):
    """
    multiply m_a and m_b
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if len(m_a) == 0 or any(not isinstance(row, list) for row in m_a):
        raise ValueError("m_a can't be empty or must be a list of lists")

    if any(any(not isinstance(el, (int, float)) for el in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")

    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("each row of m_a must be of the same size")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if len(m_b) == 0 or any(not isinstance(row, list) for row in m_b):
        raise ValueError("m_b can't be empty or must be a list of lists")

    if any(any(not isinstance(el, (int, float)) for el in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")

    if len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_b must be of the same size")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            el = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(el)
        result.append(row)

    return result

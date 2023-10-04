#!/usr/bin/python3

"""
multiply matrices module
this module contains a function that multiply matrices

"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    multiply m_a and m_b by NumPy
    """

    return (np.matmul(m_a, m_b))

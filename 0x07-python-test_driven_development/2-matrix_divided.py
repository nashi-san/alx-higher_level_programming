#!/usr/bin/python3

"""
Matrix Division Module
This module contains a function to divide all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor and returns a new matrix.
    """

    if not all(isinstance(row, list) and
               all(isinstance(elem, (int, float)) for elem in row)
               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix

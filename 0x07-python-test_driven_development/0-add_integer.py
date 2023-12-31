#!/usr/bin/python3

"""
Add module documentation.
it has one function add_integer

"""


def add_integer(a, b=98):
    """
    Adds two integers and returns the result.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return int(a + b)

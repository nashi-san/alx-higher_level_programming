#!/usr/bin/python3
"""
This is the is_kind_of_class module.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of the specified class
    or if the object is an instance of a class that inherited
    from the specified class; otherwise False.
    """

    return isinstance(obj, a_class)

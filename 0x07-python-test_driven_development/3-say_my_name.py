#!/usr/bin/python3

"""
Say My Name Module
This module contains a function that prints the given first name and last name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the given first name and last name.
    """

    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or"
                        "last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))

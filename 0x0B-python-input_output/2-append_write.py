#!/usr/bin/python3
"""
This is the append_write function.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file.
    """

    num_chars_added = 0

    with open(filename, mode='a', encoding='utf-8') as file:
        num_chars_added = file.write(text)

    return num_chars_added

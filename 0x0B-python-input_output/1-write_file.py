#!/usr/bin/python3
"""
This is the write_file function.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the number of characters written.
    """

    num_chars_written = 0
    with open(filename, mode='w', encoding='utf-8') as file:
        num_chars_written = file.write(text)

    return num_chars_written

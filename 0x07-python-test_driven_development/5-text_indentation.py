#!/usr/bin/python3

"""
Text Indentation Module
This module contains a function that print a text with 2 new lines.
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    indents with 2 new lines.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = ['.', '?', ':']
    formatted_text = ""
    remove_space = False

    for char in text:
        if char == ' ' and remove_space:
            continue

        formatted_text += char

        if char in punctuation_marks:
            formatted_text += '\n\n'
            remove_space = True
        else:
            remove_space = False

    print(formatted_text.strip())

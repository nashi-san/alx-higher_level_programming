#!/usr/bin/python3
"""
This is the append_after script.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line
    containing a specific string.
    """

    lines = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.rstrip()
            lines.append(line)
            if search_string in line:
                lines.append(new_string.rstrip())

    with open(filename, 'w') as file:
        file.write('\n'.join(lines))

#!/usr/bin/python3
"""
This is the add_item script.
"""


import json
import sys
from os import path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_item():
    """
    Adds all arguments to a Python list and saves them to a file.
    """

    filename = "add_item.json"

    if path.exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []

    items.extend(sys.argv[1:])

    save_to_json_file(items, filename)

if __name__ == "__main__":
    add_item()

#!/usr/bin/python3
"""
This is the to_json_string function.
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    """

    import json

    json_string = json.dumps(my_obj)

    return json_string

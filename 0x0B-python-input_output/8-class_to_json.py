#!/usr/bin/python3
""" My class to json module
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization.
    """

    json_dict = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value

    return json_dict

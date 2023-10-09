#!/usr/bin/python3
"""
This is the BaseGeometry module.
"""


class BaseGeometry:
    """
    Empty class representing the base geometry.
    """

    def area(self):
        """
        Raises an Exception with the message area() is not implemented.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value.
        """

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

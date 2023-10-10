#!/usr/bin/python3
""" My class module
"""


class Student:
    """
    This class represents a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance.
        """

        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }

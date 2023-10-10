#!/usr/bin/python3
"""
This is the Square module.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.
        """

        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        Computes the area of the square.
        """

        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.
        """

        return f"[Square] {self.__size}/{self.__size}"

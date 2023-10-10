#!/usr/bin/python3
"""
This is the Rectangle module.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.
        """

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        Computes the area of the rectangle.
        """

        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """

        return f"[Rectangle] {self.__width}/{self.__height}"

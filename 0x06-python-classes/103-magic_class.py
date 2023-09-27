#!/usr/bin/python3
"""This class represent the MagicClass"""
import math


class MagicClass:
    """
    This class represents the MagicClass.

    Attributes:
        __radius (float or int): The radius of the circle.

    Methods:
        __init__(radius): Initializes a MagicClass instance
            with the given radius.
        area(): Calculates and returns the area of the circle.
        circumference(): Calculates and returns the
           circumference of the circle.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance with the given radius.

        Args:
            radius (float or int): The radius of the circle.

        Raises:
            TypeError: If the radius is not a number (float or int).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius

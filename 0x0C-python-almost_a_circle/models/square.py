#!/usr/bin/python3
"""
Module: square
Contains the Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of the Square class.
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size attribute.
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.
        """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns attributes based on *args and **kwargs.
        """

        if len(args) > 0:
            self.id = args[0]

        if len(args) > 1:
            self.size = args[1]

        if len(args) > 2:
            self.x = args[2]

        if len(args) > 3:
            self.y = args[3]

        if len(args) == 0 or len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of the Square instance.
        """

        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

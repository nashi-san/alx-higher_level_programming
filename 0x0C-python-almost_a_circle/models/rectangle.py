#!/usr/bin/python3
"""
Module: rectangle
Contains the Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width attribute.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        Getter for the x attribute.
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.
        """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute.
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute.
        """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the Rectangle instance.
        """

        return self.width * self.height

    def display(self):
        """
        Prints the Rectangle instance with the character '#'.
        """

        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        """
        Assigns key/value arguments to the attributes of the
        Rectangle instance.
        """

        if len(args) > 0:
            self.id = args[0]

        if len(args) > 1:
            self.width = args[1]

        if len(args) > 2:
            self.height = args[2]

        if len(args) > 3:
            self.x = args[3]

        if len(args) > 4:
            self.y = args[4]

        if len(args) == 0 or len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.
        """

        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

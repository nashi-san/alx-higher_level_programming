#!/usr/bin/python3
"""This class represents a square"""


class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.
        """
        return self._position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character.
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)

    def __str__(self):
        """
        Prints the square using the '#' character and returns an empty string.
        """
        square_str = ""
        if self.size == 0:
            return square_str
        else:
            for _ in range(self.position[1]):
                square_str += "\n"
            for rows in range(self._size):
                square_str += (" " * self.position[0])
                square_str += ("#" * self._size)
                if (rows != self._size - 1):
                    square_str += "\n"
            return square_str

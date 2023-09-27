#!/usr/bin/python3
class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.
        """
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size
        if (len(position) != 2) or (type(position) is not tuple)\
                or (type(position[0]) is not int)\
                or (type(position[1]) is not int)\
                or (position[0] < 0) or (position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not \
                all(isinstance(i, int) for i in value) or \
                any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
                print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """
        Prints the square using the '#' character and returns an empty string.
        """
        if self.__size == 0:
            return ""
        else:
            str = ""
            self.my_print()
            for _ in range(self.position[1]):
                str += "\n"
            for _ in range(self.__size):
                str += " " * self.position[0]
                str += "#" * self.__size
                if _ != self.__size - 1:
                    str += "\n"
        return str

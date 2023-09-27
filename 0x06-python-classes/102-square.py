#!/usr/bin/python3
class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        size(): Retrieves the size of the square.
        size(value): Sets the size of the square.
        area(): Calculates and returns the current square area.
        __lt__(other): Less than comparison operator.
        __le__(other): Less than or equal to comparison operator.
        __eq__(other): Equality comparison operator.
        __ne__(other): Not equal to comparison operator.
        __gt__(other): Greater than comparison operator.
        __ge__(other): Greater than or equal to comparison operator.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __lt__(self, other):
        """
        Less than comparison operator.

        Args:
            other (Square): The other square object to compare.

        Returns:
            bool: True if the area of the current square is less than
            the area of the other square, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        Less than or equal to comparison operator.

        Args:
            other (Square): The other square object to compare.

        Returns:
            bool: True if the area of the current square is less than
                or equal to the area of the other square, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __eq__(self, other):
        """
        Equality comparison operator.

        Args:
            other (Square): The other square object to compare.

        Returns:
            bool: True if the area of the current square is equal
                to the area of the other square, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """
        Not equal to comparison operator.

        Args:
            other (Square): The other square object to compare.

        Returns:
            bool: True if the area of the current square is not equal
                to the area of the other square, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __gt__(self, other):
        """
        Greater than comparison operator.

        Args:
            other (Square): The other square object to compare.

        Returns:
            bool: True if the area of the current square is greater than
                the area of the other square, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        Greater than or equal to comparison operator.

        Args:
            other (Square): The other square object to compare.

        Returns:
            bool: True if the area of the current square is greater than
                or equal to the area of the other square, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

#!/usr/bin/python3
"""Module class for testing square classe"""


import unittest
import pep8
import os
from io import StringIO
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """A class for testing square classe
    """

    def test_size_getter(self):
        """
        Test the getter for the size attribute.
        """

        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_size_setter(self):
        """
        Test the setter for the size attribute.
        """

        square = Square(5)
        square.size = 8
        self.assertEqual(square.size, 8)

    def test_size_setter_invalid_type(self):
        """
        Test the setter for the size attribute with an invalid type.
        """

        square = Square(5)
        with self.assertRaises(TypeError):
            square.size = "invalid"

    def test_size_setter_invalid_value(self):
        """
        Test the setter for the size attribute with an invalid value.
        """

        square = Square(5)
        with self.assertRaises(ValueError):
            square.size = -5

    def test_area(self):
        """Test the area method of the Square class.
        """

        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_display(self):
        """Test the display method of the Square class.
        """

        square = Square(5)
        expected_output = "#####\n" \
                          "#####\n" \
                          "#####\n" \
                          "#####\n" \
                          "#####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            square.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_update(self):
        """
        Test the update method of the Square class.
        """

        square = Square(5)
        square.update(1, 8, 3, 4)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_update_with_args(self):
        """Test the update method of the Square class with
        positional arguments.
        """

        square = Square(5)
        square.update(1, 8, 3, 4)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_update_with_kwargs(self):
        """
        Test the update method of the Square class with keyword
        arguments.
        """

        square = Square(5)
        square.update(id=1, size=8, x=3, y=4)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_str(self):
        """
        Test the __str__ method of the Square class.
        """

        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_to_dictionary(self):
        """
        Test the to_dictionary method of the Square class.
        """

        square = Square(5, 2, 3, 1)
        square_dict = square.to_dictionary()
        self.assertEqual(square_dict, {'x': 2, 'y': 3, 'id': 1, 'size': 5})


if __name__ == '__main__':
    unittest.main()

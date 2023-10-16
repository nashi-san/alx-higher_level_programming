#!/usr/bin/python3
"""Module class for testing rectangle classe"""
import unittest
import pep8
import os
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """A class for testing rectangle classe"""

    def test_width_getter(self):
        """
        Test the getter for the width attribute.
        """
        rect = Rectangle(5, 10)
        self.assertEqual(rect.width, 5)

    def test_width_setter(self):
        """
        Test the setter for the width attribute.
        """
        rect = Rectangle(5, 10)
        rect.width = 8
        self.assertEqual(rect.width, 8)

    def test_width_setter_invalid_type(self):
        """
        Test the setter for the width attribute with an invalid type.
        """
        rect = Rectangle(5, 10)
        with self.assertRaises(TypeError):
            rect.width = "invalid"

    def test_width_setter_invalid_value(self):
        """
        Test the setter for the width attribute with an invalid value.
        """
        rect = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            rect.width = -5

    def test_height_getter(self):
        """
        Test the getter for the height attribute.
        """
        rect = Rectangle(5, 10)
        self.assertEqual(rect.height, 10)

    def test_height_setter(self):
        """
        Test the setter for the height attribute.
        """
        rect = Rectangle(5, 10)
        rect.height = 12
        self.assertEqual(rect.height, 12)

    def test_height_setter_invalid_type(self):
        """
        Test the setter for the height attribute with an invalid type.
        """
        rect = Rectangle(5, 10)
        with self.assertRaises(TypeError):
            rect.height = "invalid"

    def test_height_setter_invalid_value(self):
        """
        Test the setter for the height attribute with an invalid value.
        """
        rect = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            rect.height = -10

    def test_x_getter(self):
        """
        Test the getter for the x attribute.
        """
        rect = Rectangle(5, 10, 2, 3)
        self.assertEqual(rect.x, 2)

    def test_x_setter(self):
        """
        Test the setter for the x attribute.
        """
        rect = Rectangle(5, 10, 2, 3)
        rect.x = 4
        self.assertEqual(rect.x, 4)

    def test_x_setter_invalid_type(self):
        """
        Test the setter for the x attribute with an invalid type.
        """
        rect = Rectangle(5, 10, 2, 3)
        with self.assertRaises(TypeError):
            rect.x = "invalid"

    def test_x_setter_invalid_value(self):
        """
        Test the setter for the x attribute with an invalid value.
        """
        rect = Rectangle(5, 10, 2, 3)
        with self.assertRaises(ValueError):
            rect.x = -2

    def test_y_getter(self):
        """
        Test the getter for the y attribute.
        """
        rect = Rectangle(5, 10, 2, 3)
        self.assertEqual(rect.y, 3)

    def test_y_setter(self):
        """
        Test the setter for the y attribute.
        """
        rect = Rectangle(5, 10, 2, 3)
        rect.y = 5
        self.assertEqual(rect.y, 5)

    def test_y_setter_invalid_type(self):
        """
        Test the setter for the y attribute with an invalid type.
        """
        rect = Rectangle(5, 10, 2, 3)
        with self.assertRaises(TypeError):
            rect.y = "invalid"

    def test_y_setter_invalid_value(self):
        """
        Test the setter for the y attribute with an invalid value.
        """
        rect = Rectangle(5, 10, 2, 3)
        with self.assertRaises(ValueError):
            rect.y = -3

    def test_area(self):
        """
        Test the area method of the Rectangle class.
        """
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        """
        Test the display method of the Rectangle class.
        """
        rect = Rectangle(5, 10)
        rect.display()

    def test_update(self):
        """
        Test the update method of the Rectangle class.
        """
        rect = Rectangle(5, 10)
        rect.update(1, 8, 12, 3, 4)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 12)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_to_dictionary(self):
        """
        Test the to_dictionary method of the Rectangle class.
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        rect_dict = rect.to_dictionary()
        self.assertEqual(rect_dict, {'x': 2, 'y': 3, 'id': 1, 'height': 10, 'width': 5})


if __name__ == '__main__':
    unittest.main()

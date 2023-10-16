#!/usr/bin/python3
"""Module class for testing Base classe"""


import unittest
import pep8
import os
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestBase(unittest.TestCase):
    """A class for testing base classe
    """

    def test_pep8_conformance(self):
        """Test that the code conforms to PEP8.
        """

        style = pep8.StyleGuide()
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style errors found")

    def test_init_with_id(self):
        """Test the __init__ method with passing an id.
        """

        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_to_json_string_empty(self):
        """Test the to_json_string method with an empty list.
        """

        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        """
        Test the to_json_string method with a list of dictionaries.
        """
        objs = [{"id": 1, "name": "object1"}, {"id": 2, "name": "object2"}]
        json_string = Base.to_json_string(objs)
        expected_json = (
            '[{"id": 1, "name": "object1"}, '
            '{"id": 2, "name": "object2"}]'
        )
        self.assertEqual(json_string, expected_json)

    def test_from_json_string_empty(self):
        """Test the from_json_string method with an empty string.
        """

        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string(self):
        """Test the from_json_string method with a json string.
        """

        json_string = (
            '[{"id": 1, "name": "object1"}, '
            '{"id": 2, "name": "object2"}]'
        )
        objs = Base.from_json_string(json_string)
        self.assertEqual(
            objs,
            [{"id": 1, "name": "object1"}, {"id": 2, "name": "object2"}]
        )

    def test_create_rectangle(self):
        """Test the create method for Rectangle class.
        """

        rect_dict = {"id": 1, "width": 10, "height": 5}
        rect = Rectangle.create(**rect_dict)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 5)

    def test_create_square(self):
        """Test the create method for Square class.
        """

        square_dict = {"id": 1, "size": 5}
        square = Square.create(**square_dict)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 5)

    def test_load_from_file_not_found(self):
        """Test the load_from_file method when the file is not found.
        """

        objs = Base.load_from_file()
        self.assertEqual(objs, [])

    def test_load_from_file_csv_not_found(self):
        """Test the load_from_file_csv method when the file is not found.
        """

        objs = Base.load_from_file_csv()
        self.assertEqual(objs, [])


if __name__ == '__main__':
    unittest.main()

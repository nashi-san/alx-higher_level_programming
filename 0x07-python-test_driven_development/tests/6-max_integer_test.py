#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Creates unittests for max_integer([..])."""

    def test_max_integer(self):
        """ Test with a list of integers"""

        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([10, 20, 30, 40, 50]), 50)

    def test_max_integer_empty_list(self):
        """ Test with an empty list"""

        self.assertIsNone(max_integer([]))

    def test_max_integer_duplicate_values(self):
        """ Test with a list containing duplicate values"""

        self.assertEqual(max_integer([1, 2, 3, 3, 2, 1]), 3)
        self.assertEqual(max_integer([10, 20, 30, 30, 20, 10]), 30)

    def test_max_integer_negative_values(self):
        """ Test with a list containing negative values"""

        self.assertEqual(max_integer([-5, -10, -2, -1, -3]), -1)
        self.assertEqual(max_integer([-100, -200, -300, -400]), -100)


if __name__ == '__main__':
    unittest.main()

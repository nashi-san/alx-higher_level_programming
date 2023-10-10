#!/usr/bin/python3
"""
This is MyInt module.
"""


class MyInt(int):
    """
    Represents a rebel integer.
    """

    def __eq__(self, other):
        """
        Inverts the == operator.
        """

        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator.
        """

        return super().__eq__(other)

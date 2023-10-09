#!/usr/bin/python3
""" a class MyList that inherits from list """


class MyList(list):
    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.
        """
        print(sorted(self))

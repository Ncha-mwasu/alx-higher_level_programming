#!/bin/python3
"""
A class module to sort lists in ascending order
"""


class MyList(list):
    """
    A python class (blueprint) that prints a list in sorted order

    Args:
        list: a list of int.
    """

    def print_sorted(self):
        """
        A class method that prints a list in sorted order
        """
        list_sorted = self.copy()
        list_sorted.sort()
        print(list_sorted)

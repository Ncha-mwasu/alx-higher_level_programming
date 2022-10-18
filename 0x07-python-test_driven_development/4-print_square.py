#!/usr/bin/python3
"""
A square printing module
"""


def print_square(size):
    """This function computes one's full name using two strings
    Args:
        size: an integer

    Raises:
        TypeError: If size is not of int type
        ValueError: If size is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()

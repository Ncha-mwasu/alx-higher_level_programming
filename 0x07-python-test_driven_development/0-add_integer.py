#!/usr/bin/python3
"""An addition module"""


def add_integer(a, b=98):
    """This function adds two numbers [integer(s) and/or float(s)]
    Args:
        a: first number
        b: second number

    Return:
        The sum of the two numbers in integer format.

    Raises:
        TypeError: If a and/or b is/are not (an) integer(s)
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return(int(a) + int(b))

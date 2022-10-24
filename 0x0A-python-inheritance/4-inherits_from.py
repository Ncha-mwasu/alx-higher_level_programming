#!/usr/bin/python3
"""
A function that checks for only inheritance.
"""


def inherits_from(obj, a_class):
    """
    A function that returns True if the object is an instance
    of a class that inherited (directly or indirectly) from
    the specified class ; otherwise False.

    Args:
        obj: an instance of a class.
        a_class: a class.

    Returns:
        True: if obj is a sub class of a_class
        False: if not
    """

    return type(obj) != a_class and isinstance(obj, a_class)

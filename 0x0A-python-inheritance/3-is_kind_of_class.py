#!/usr/bin/python3
"""
A functon that checks for inheritence
"""


def is_kind_of_class(obj, a_class):
    """
    A function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.

    Args:
        obj: an instance of a class.
        a_class: a class.

    Returns:
        True: if obj is an instance of / obj of an instance
                inherited from.
        False: if not
    """

    return isinstance(obj, a_class)

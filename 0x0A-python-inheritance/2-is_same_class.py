#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    A function that returns True if the object is exactly
    an instance of the specified class ; otherwise False

    Args:
        obj: an instance of a class.
        a_class: a class.

    Returns:
        True: if obj is of type a_class
        False: if not
    """

    return type(obj) is a_class

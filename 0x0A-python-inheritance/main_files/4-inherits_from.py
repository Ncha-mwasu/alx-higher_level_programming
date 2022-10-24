#!/usr/bin/python3

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

    return issubclass(a_class.obj, a_class)

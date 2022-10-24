#!/usr/bin/python3
def lookup(obj):
    """
    method returning all properties and methods
    of the specified object, without the values

    Args:
        Obj: a class instance

    Returns:
        The properties and methods of the specified object
    """

    return dir(obj)

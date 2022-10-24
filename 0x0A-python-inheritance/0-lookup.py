#!/usr/bin/python3
def lookup(obj):
    """
    Function returning all properties and methods
    of the specified object, without the values

    Args:
        Obj: The class' instance

    Returns:
        List of properties and methods of the specified object
    """

    return (dir(obj))

#!/usr/bin/python3
"""Defining a class square"""

class Square:
    """Class square a blueprint (definition) for a square object
    """
    def __init__(self, size):
        """__init__ Class Initialization method that stores the size of the square
        Args:
            size (int): size of the square
        """
        self.__size = size

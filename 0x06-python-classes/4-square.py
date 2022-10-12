#!/usr/bin/python3
"""Defining a class square"""


class Square:
    """Class square a blueprint (definition) for a square object
    """

    def __init__(self, size=0):
        """method that stores the size of the square
        Args:
            param1 (int): the size of the square
        """
        if not isinstance(size, int):
            raise Exception("size must be an integer")

        elif size < 0:
            raise Exception("size must be >= 0")

        else:
            self.__size = size

    def area(self):
        """Class methods to calculate the area of square

        Returns:
            area of size

        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ method to get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """method to set the size of the square"""

        if not isinstance(value, int):
            raise Exception("size must be an integer")

        elif value < 0:
            raise Exception("size must be >= 0")

        else:
            self.__value = value

#!/usr/bin/python3
"""Defining a class square"""


class Square:
    """Class square a blueprint (definition) for a square object"""

    def __init__(self, size=0):
        """method that stores the size of the square
        Args:
            size (int): the size of the square
        """
        self.__size = size

    @property
    def size(self):
        """ method to get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """method to set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__value = value

    def area(self):
        """Class methods to calculate the area of square
        Return area of size
        """
        return (self.__size ** 2)

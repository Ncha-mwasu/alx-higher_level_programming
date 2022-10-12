#!/usr/bin/python3
"""Defining a class square"""


class Square:
    """Class square a blueprint for a square object
    """
    def __init__(self, size=0):
        """Initialization method that stores the size of the square
        Args:
            size (int): the size of the square
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
            True if successful, False otherwise.
        """
        return (self.__size ** 2)

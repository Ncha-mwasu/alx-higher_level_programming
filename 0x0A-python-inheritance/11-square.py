#!/usr/bin/python3
"""
Implementing a square class using rectangle
as a base/parent class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A blueprint Rectangle class defined by its parent class
    Base geometry
    """

    def __init__(self, size):
        """
        Initialization of the class
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        The square class return value
        """
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))

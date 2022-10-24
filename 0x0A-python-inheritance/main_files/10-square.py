#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
    A class of name Square
"""


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

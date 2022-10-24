#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
    A class of name Rectangle
"""


class Rectangle(BaseGeometry):
    """
    A blueprint Rectangle class defined by its parent class
    Base geometry
    """

    def __init__(self, width, height):
        """
        Initialization of the class
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

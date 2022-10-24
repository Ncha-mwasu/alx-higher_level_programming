#!/usr/bin/python3
"""
Implementing the geometry class
by defining a rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

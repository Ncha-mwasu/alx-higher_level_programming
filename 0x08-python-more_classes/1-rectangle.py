#!/usr/bin/python3
"""A rectangle class (blueprint).
"""


class Rectangle:
    """
    A class (blueprint) to create a rectangle.
    """
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Method to get the width of the triangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Method to set the width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ 
        Method to get the height of the rectangle
        """
        return self.__height

    @height.setter
    """
    Method to set the height of the rectangle 
    """
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

#!/usr/bin/python3
"""
    A class of name BaseGeometry
"""


class BaseGeometry:
    """
    A blue print parents class
    """

    def area(self):
        """
        Method to ge the area of a geometric figure

        Raise:
            Exception: if area is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method to check if value is an integer

        Raises:
            TypeError: if value is not of int type
            ValueError: if value is less than or equal to zero
        """

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")

        if value <= 0:
            raise ValueError("<name> must be greater than 0")

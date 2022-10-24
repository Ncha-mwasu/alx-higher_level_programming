#!/usr/bin/python3
"""
A user defined int class inheriting
from the built-in int class
"""


class MyInt(int):
    """
    MyInt class to invert '==' and '!=' operators
    """
    
    def __eq__(self, other):
        """
        method that inverts '==' by returning '!='
        """
        return self.real != other

    def __ne__(self, other):
        """
        function that invert '!=' by returning '=='
        """
        return self.real == other

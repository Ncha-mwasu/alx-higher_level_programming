#!/usr/bin/python3
"""
A in class
"""

class MyInt(int):
    """
    MyInt class inheriting from the int class
    """
    
    def __eq__(self, other):
        """
        method that inverts '==' by returning '!='
        """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """
        function that invert '!=' by returning '=='
        """
        return int.__eq__(self, other)

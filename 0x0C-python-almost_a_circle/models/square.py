#!/usr/bin/python3
"""
Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializing the Square class
        """
        super().__init__(size, size, x, y, id=None)

    def __str__(self):
        """
        The rectangle class return statement
        """
        out = "[Square]"
        output = " ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
        return out + output

    @property
    def size(self):
        """
        Method to get the width of the square

        Returns:
            The width value of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Method to set the width of the square

        Args:
            value (int): a set width value.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.width = value

    def update(self, *args, **kwargs):
        """
        Update method: updates the values of the instance variable
        """
        if args is not None and len(args) != 0:
            list_attr = ["id", "size", "x", "y"]

            for arg in range(len(args)):
                setattr(self, list_attr[arg], args[arg])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Method to pass instance variables as a dictionary
        """
        list_attr = ["id", "size", "x", "y"]

        sqr_dict = {}
        for key in list_attr:
            if key == "size":
                sqr_dict[key] = getattr(self, "width")
            else:
                sqr_dict[key] = getattr(self, key)
        return sqr_dict

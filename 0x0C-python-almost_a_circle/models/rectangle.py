"""
Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializing the rectangle class
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(id)

    @property
    def width(self):
        """
        Method to get the width of the triangle

        Returns:
            The width value of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Method to set the width of the rectangle

        Args:
          value (int): a set width value.
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

        Returns:
            The height value of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Method to set the height of the rectangle

        Args:
            value (int): a set height value.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        Method to get x

        Returns:
            The x value
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Method to set x

        Args:
            value (int): a set x value.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        Method to get y

        Returns:
            The y value
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Method to set y

        Args:
            value (int): a set y value.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Method to compute the
        area of the rectangle
        """

        return self.__height * self.__width

    def display(self):
        """
        Method that prints rectangle using "#"
        """
        output = ""
        output = self.__y * "\n"
        for i in range(self.__height):
            output += (" " * self.__x)
            output += ("#" * self.__width) + "\n"
        print(output[:-1])

    def __str__(self):
        """
        The rectangle class return statement
        """
        output = "[Rectangle]"
        output1 = " ({}) {}/{}".format(self.id, self.__x, self.__y)
        output2 = " - {}/{}".format(self.__width, self.__height)
        return output + output1 + output2

    def update(self, *args, **kwargs):
        """
        Update method: updates the values of the instance variable
        """
        if args is not None and len(args) != 0:
            list_attr = ['id', 'width', 'height', 'x', 'y']
            for attr in range(len(args)):
                setattr(self, list_attr[attr], args[attr])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Method to pass instance variables as a dictionary
        """
        list_attr = ["id", "size", "x", "y"]

        rect_dict = {}
        for key in list_attr:
            if key == "size":
                rect_dict[key] = getattr(self, "width")
            else:
                rect_dict[key] = getattr(self, key)
        return rect_dict

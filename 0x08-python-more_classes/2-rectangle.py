#!/usr/bin/python3

"""THIS FILE IS USED TO Define RECTANGLE CLASS."""


class Rectangle:
    """A CLASS THAT REPRESENTS A RECTANGLE."""

    def __init__(self, width=0, height=0):
        """FUNCTION USED TO Initialize A NEW RECTANGLE.

        Args:
            height (int): HEIGHT OF NEW RECTANGLE.
            width (int): WIDTH OF NEW RECTANGLE.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """A FUNCTION USED TO GET THE WIDTH."""

        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """A FUNCTION USED TO GET THE HEIGHT."""

        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):

        """A FUNCTION USED TO RETURN AREA OF RECTANGLE."""

        return (self.__width * self.__height)

    def perimeter(self):

        """A FUNCTION USED TO RETURN AREA OF RECTANGLE."""

        if self.__height == 0 or self.__width == 0:
            return (0)

        return ((self.__width * 2) + (self.__height * 2))

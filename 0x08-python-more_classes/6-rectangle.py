#!/usr/bin/python3

"""THIS FILE IS USED TO Define RECTANGLE CLASS."""


class Rectangle:
    """A CLASS THAT REPRESENTS A RECTANGLE.

    Attributes:
      number_of_instances (int): REPRESENTS NUM OF RECTANGLE INSTANCE."""

    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """FUNCTION USED TO Initialize A NEW RECTANGLE.

        Args:
            height (int): HEIGHT OF NEW RECTANGLE.
            width (int): WIDTH OF NEW RECTANGLE.
        """

        type(self).number_of_instances += 1
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

    def __str__(self):
        """A FUNCTION USED TO RETURN A REPRESENTATION THAT'S.

        PRINTABLE USING THE HASHTAG SIGN('#').
        """

        if self.__height == 0 or self.__width == 0:
            return ("")

        RECTANGLE = []

        for n in range(self.__height):
            [RECTANGLE.append('#') for k in range(self.__width)]
            if n != self.__height - 1:

                RECTANGLE.append("\n")

        return ("".join(RECTANGLE))

    def __repr__(self):

        """A FUCNTION THAT IS USED TO REPRESENT
        IT USING A STRING FOR THE RECTANGLE."""

        RECTANGLE = "Rectangle(" + str(self.__width)
        RECTANGLE += ", " + str(self.__height) + ")"

        return (RECTANGLE)

    def __del__(self):
        """A FUNCTION THAT IS USED TO DISPLAY A MESSAGE FOR DELETING
        EVERY SINGLE TIME FOR THE RECTANGLE."""

        type(self).number_of_instances -= 1
        print("Bye rectangle...")

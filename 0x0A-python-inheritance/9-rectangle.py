#!/usr/bin/python3

"""THIS PYTHON IS USED TO DEFINE
A class Rectangle THAT INHERITS
FROM BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A CLASS THAT REPRESENTS A rectangle
    BY USING BaseGeometry."""

    def __init__(self, width, height):
        """USED TO Intialize A NEW Rectangle.

        Args:
            width (int): REPRESENTS THE WIDTH.
            height (int): REPRESENTS THE HEIGHT.
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """A FUNCTION THAT IS USED TO RETURN
        THE area OF THE rectangle."""

        return self.__width * self.__height

    def __str__(self):
        """A FUNCTION THAT IS USED TO RETURN
        THE print() AND str() REPRESENTATION
        OF A RECTANGLE."""

        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string

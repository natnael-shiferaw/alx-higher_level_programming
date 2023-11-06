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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

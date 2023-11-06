#!/usr/bin/python3

"""THIS PYTHON FILE IS USED TO DEFINE
a Rectangle subclass Square."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A CLASS THAT IS USED TO REPRESENT a square."""

    def __init__(self, size):
        """USED TO Initialize A NEW square.

        Args:
            size (int): REPRESENTS THE SIZE.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

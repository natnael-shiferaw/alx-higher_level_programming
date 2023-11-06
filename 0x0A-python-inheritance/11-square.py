#!/usr/bin/python3

"""A PYTHON FILE THAT IS USED TO DEFINE
a Rectangle subclass Square."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A CLASS THAT REPRESENTS a square."""

    def __init__(self, size):
        """USED TO Initialize A NEW square.

        Args:
            size (int): REPRESENTS The size.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)

        self.__size = size

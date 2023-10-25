#!/usr/bin/python3
"""This file Defines a class named Square."""


class Square:
    """It is used to represent a square."""

    def __init__(self, size=0):
        """A function used to Initialize a new square.

        Args:
            size (int): represents the SIZE of the new square.
        """

        self.size = size

    @property
    def size(self):
        """used to FETCH the CURRENT AREA of the square."""

        return (self.__size)

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """FUNCTION USED TO Return the CURRENT AREA of the square."""

        return (self.__size * self.__size)

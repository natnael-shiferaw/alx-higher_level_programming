#!/usr/bin/python3
"""This file Defines a class named Square."""


class Square:
    """USED TO Represent a square."""

    def __init__(self, size):
        """A FUNCTION THAT Initializes a new square.

        Args:
            size (int): REPRESENTS THE SIZE OF the new square.
        """

        self.size = size

    @property
    def size(self):
        """A FUCNTION THAT FETCHES CURRENT SIZE OF the square."""

        return (self.__size)

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """USED TO RETURN THE CURRENT AREA OF THE SQUARE."""

        return (self.__size * self.__size)

    def my_print(self):
        """A FUNCTION THAT PRINTS SQUARE USING #."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")

        if self.__size == 0:
            print("")

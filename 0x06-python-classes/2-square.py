#!/usr/bin/python3
"""This file Defines a class named Square."""


class Square:
    """It is used to Represent a square."""

    def __init__(self, size=0):
        """A fucntion that Initializes a new Square.

        Args:
            size (int): It represents the size of the new square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

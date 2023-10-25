#!/usr/bin/python3
"""A FILE THAT DEFINES A class NAMED Square."""


class Square:
    """A CLASS THAT REPRESENTS A square."""

    def __init__(self, size=0):
        """USED TO Initialize a NEW square.

        Args:
            size (int): REPRESENTS THE SIZE OF the NEW square.
        """

        self.size = size

    @property
    def size(self):
        """A FUCNTION THAT FETCHES THE CURRENT SIZE OF the square."""

        return (self.__size)

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """A FUNCTION THAT RETURNS THE CURRENT AREA OF the square."""

        return (self.__size * self.__size)

    def __eq__(self, other):
        """A FUCNTION THAT DEFINES the EQUALTO COMPARISSIONto a Square."""

        return self.area() == other.area()

    def __ne__(self, other):
        """A FUCNTION THAT DEFINES the NOT EQUALTO COMPARISSIONto a Square."""

        return self.area() != other.area()

    def __lt__(self, other):
        """A FUCNTION THAT DEFINES the LESSTHAN COMPARISSIONto a Square."""

        return self.area() < other.area()

    def __le__(self, other):
        """A FUCNTION THAT DEFINES the LESSTHAN
        OR EQUALTO COMPARISSIONto a Square."""

        return self.area() <= other.area()

    def __gt__(self, other):
        """A FUCNTION THAT DEFINES the GREATERTHAN COMPARISSION to a Square."""

        return self.area() > other.area()

    def __ge__(self, other):
        """A FUCNTION THAT DEFINES the GREATERTHAN
        OR EQUALTO COMPARISSION to a Square."""

        return self.area() >= other.area()

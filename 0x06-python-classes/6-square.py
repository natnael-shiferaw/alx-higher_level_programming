#!/usr/bin/python3
"""THIS FILE DEFINES a class NAMED Square."""


class Square:
    """USED TO REPRESENT a square."""

    def __init__(self, size=0, position=(0, 0)):
        """A FUNCTION Initializes A NEW square.

        Args:
            size (int): REPRESENTS THE SIZE OF the NEW square.
            position (int, int): REPRESENTS THE POSITION OF the NEW square.
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """A FUNCTION THAT FETCHES CURRENT SIZE OF the square."""

        return (self.__size)

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """A FUNCTION THAT FETCHES CURRENT POSITION OF THE SQUARE."""

        return (self.__position)

    @position.setter
    def position(self, value):

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """A FUNCTION THAT RETURNS THE CURRENT AREA OF the square."""

        return (self.__size * self.__size)

    def my_print(self):
        """A FUNCTION THAT PRINT SQUARE USING #."""

        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]

        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

#!/usr/bin/python3
"""A FILE THAT DEFINES A MagicClass THAT PERFORMS
ACTIONS BASED ON THE PYTHON BYTECODE."""

import math


class MagicClass:
    """A CLASS THAT IS USED TO REPRESENT A CIRCLE."""

    def __init__(self, radius=0):
        """USED TO Initialize a MagicClass.

        Arg:
            radius (float or int): REPRESENTS THE RADIUS OF NEW MagicClass.
        """

        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """A FUNCTION THAT RETURNS THE AREA OF the MagicClass."""

        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """A FUNCTION THAT RETURNS THE CIRCUMFERENCE OF THE MagicClass."""

        return (2 * math.pi * self.__radius)

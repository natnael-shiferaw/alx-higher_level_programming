#!/usr/bin/python3

"""A PYTHON FILE THAT IS USED TO DEFINE
A BASE GEOMETRY class BaseGeometry,
public instance methods."""


class BaseGeometry:
    """A CLASS WITH PUBLIC INSTANCE METHODS."""

    def area(self):
        """IT'S NOT IMPLEMENTED YET."""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """A FUNCTION THAT VALIDATES value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

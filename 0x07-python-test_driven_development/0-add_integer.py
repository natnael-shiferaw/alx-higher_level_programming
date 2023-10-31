#!/usr/bin/python3
"""THIS PYTHON FILE DEFINES A FUNCTION THAT IS USED TO ADD INTEGERS."""


def add_integer(a, b=98):
    """A FUCNTION THAT RETURNS THE ADDITION OF a AND b.

    BEFORE ADDITION FLOAT ARE CHANGED TO INTEGERS.

    Raises:
        TypeError: IF ONE OF THEM(a,b) ARE NOT INTEGER OR FLOAT.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")

    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))

#!/usr/bin/python3
"""A PYTHON FILE THAT DEFINES A FUNCTION THAT IS USED
FOR PRINTING A SQUARE USING A CHARACTER."""


def print_square(size):
    """A FUCNTION USED TO PRINT A SQUARE USING #.

    Args:
        size (int): REPRESENTS HEIGHT/WIDTH OF SQUARE.
    Raises:
        TypeError: IF size IS ANYTHING OTHER THAN INTEGER.
        ValueError: IF size IS LESS THAN 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for N in range(size):
        [print("#", end="") for K in range(size)]
        print("")

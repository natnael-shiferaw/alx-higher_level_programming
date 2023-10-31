#!/usr/bin/python3
"""THIS IS A PYTHION FILE THAT DEFINES A FUNCTION
THAT IS USED FOR PRINTING NAME."""


def say_my_name(first_name, last_name=""):
    """A FUNCTION THAT IS USED TO PRINT A NAME.

    Args:
        first_name (str): FIRST NAME TO BE PRINTED.
        last_name (str): LAST NAME TO BE PRINTED.
    Raises:
        TypeError: IF THE NAMES ARE ANYTHING OTHER THAN STRING.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

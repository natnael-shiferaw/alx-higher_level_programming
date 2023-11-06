#!/usr/bin/python3

"""A PYTHON FILE THAT IS USED TO DEFINE
A FUNCTION FOR ADDING attributes TO objects."""


def add_attribute(obj, att, value):
    """A FUNCTION THAT IS USED TO ADD
    A NEW attribute TO AN object if feasible.

    Args:
        obj (any): represents the object.
        att (str): represents the name of the attribute.
        value (any): represents The value of att.
    Raises:
        TypeError: IF THE attribute CAN'T BE ADDED.
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, att, value)

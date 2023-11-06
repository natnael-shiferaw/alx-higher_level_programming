#!/usr/bin/python3

"""THIS PYTHON FILE IS USED TO DEFINE
A FUNCTION FOR INHERITED class-checking."""


def inherits_from(obj, a_class):
    """A FUNCTION THAT CHECKS IF AN OBJECT
    IS AN INHERITED INSTANCE OF A GIVEN class.

    Args:
        obj (any): REPRESENTS THE OBJECT.
        a_class (type): REPRESENTS THE class
        TO MATCH WITH THE obj.
    Returns:
        True - IF obj IS AN INHERITED
        INSTANCE OF a_class.
        False - Otherwise.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

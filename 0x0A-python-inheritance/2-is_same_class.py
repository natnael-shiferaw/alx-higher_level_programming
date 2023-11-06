#!/usr/bin/python3

"""THIS PYTHON FILE IS USED TO DEFINE
A FUNCTION THAT'S USED FOR class-checking."""


def is_same_class(obj, a_class):
    """A FUNCTION THAT CHECKS IF AN OBJECT
    IS AN INSTANCE OF A GIVEN class.

    Args:
        obj (any): REPRESENTS THE OBJECT.
        a_class (type): REPRESENTS THE class
        TO MATCH WITH THE obj.
    Returns:
        True - IF obj IS INSTANCE OF a_class.
        False - Otherwise.
    """

    if type(obj) == a_class:
        return True
    return False

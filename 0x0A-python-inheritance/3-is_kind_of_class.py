#!/usr/bin/python3

"""THIS PYTHON FILE IS USED TO DEFINE
A class AND A FUNCTION OF INHERITED
class-checking."""


def is_kind_of_class(obj, a_class):
    """A FUNCTION THAT IS USED TO CHECK
    WHETHER AN OBJECT IS AN INSTANCE OR
    INHERITED INSTANCE OF A class.

    Args:
        obj (any): REPRESENTS THE object.
        a_class (type): REPRESENTS THE class
        TO MATCH WITH THE obj.
    Returns:
        True - IF obj IS INSTANCE/INHERITED
        INSTANCE OF a_class.
        False - Otherwise.
    """

    if isinstance(obj, a_class):
        return True
    return False

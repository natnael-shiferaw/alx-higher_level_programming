#!/usr/bin/python3
"""A MODULE THAT IS USED FOR THE PUPRPOSE OF
FINDING THE MAXIMUM INTEGER FROM A GIVEN LIST.
"""


def max_integer(list=[]):
    """A FUNCTION THAT IS USED TO FIND THE MAXIMUM INTEGER
    FROM A LIST, RETRUNS None IF THE LIST IS EMPTY.
    """

    if len(list) == 0:
        return None
    RES = list[0]
    J = 1

    while J < len(list):

        if list[J] > RES:
            RES = list[J]
        J += 1

    return RES

#!/usr/bin/python3


def no_c(my_string):

    """This program is used to remove the
    characters c and C from a string."""

    cpy = [n for n in my_string if n != 'c' and n != 'C']
    return ("".join(cpy))

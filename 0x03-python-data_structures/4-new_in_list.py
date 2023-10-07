#!/usr/bin/python3


def new_in_list(my_list, idx, element):

    """This program is used to replace an
    element in a copied list at a particular position."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    cpy = [n for n in my_list]
    cpy[idx] = element
    return (cpy)

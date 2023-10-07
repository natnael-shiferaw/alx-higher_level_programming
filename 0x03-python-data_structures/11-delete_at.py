#!/usr/bin/python3


def delete_at(my_list=[], idx=0):

    """This program is used delete an item
    at a particular position in the list."""
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)

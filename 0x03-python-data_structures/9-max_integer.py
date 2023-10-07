#!/usr/bin/python3


def max_integer(my_list=[]):

    """This program is used to find the biggest integer in the list."""
    if len(my_list) == 0:
        return (None)

    biggest = my_list[0]
    for n in range(len(my_list)):
        if my_list[n] > biggest:
            biggest = my_list[n]

    return (biggest)

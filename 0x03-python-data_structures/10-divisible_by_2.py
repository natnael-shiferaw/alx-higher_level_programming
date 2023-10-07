#!/usr/bin/python3


def divisible_by_2(my_list=[]):

    """This program is used to find all the multiples of 2 in the list."""
    Multiples = []
    for n in range(len(my_list)):
        if my_list[n] % 2 == 0:
            Multiples.append(True)
        else:
            Multiples.append(False)

    return (Multiples)

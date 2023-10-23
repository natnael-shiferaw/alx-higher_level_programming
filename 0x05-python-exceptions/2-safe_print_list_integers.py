#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):

    """Print the first n integer elements of a list."""

    num_of_elem = 0
    for n in range(0, x):
        try:
            print("{:d}".format(my_list[n]), end="")
            num_of_elem += 1
        except (ValueError, TypeError):
            continue
    print("")
    return num_of_elem

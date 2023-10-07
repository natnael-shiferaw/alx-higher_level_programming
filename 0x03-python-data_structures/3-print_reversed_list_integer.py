#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):

    """This program is used to print all the integers
    in a list in a reverse order."""

    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))

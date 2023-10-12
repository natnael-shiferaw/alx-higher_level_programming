#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):

    list_order = list(a_dictionary.keys())
    list_order.sort()

    for n in list_order:
        print("{}: {}".format(n, a_dictionary.get(n)))

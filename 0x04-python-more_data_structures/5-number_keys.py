#!/usr/bin/python3


def number_keys(a_dictionary):

    number = 0
    list_keys = list(a_dictionary.keys())

    for n in list_keys:
        number += 1

    return (number)

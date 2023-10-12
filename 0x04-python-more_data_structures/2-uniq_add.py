#!/usr/bin/python3


def uniq_add(my_list=[]):

    uniqe_list = set(my_list)
    number = 0

    for n in uniqe_list:
        number += n

    return (number)

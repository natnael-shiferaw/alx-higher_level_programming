#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    num_of_elem = 0  # number of elements
    for n in range(x):
        try:
            print("{}".format(my_list[n]), end="")
            num_of_elem += 1
        except IndexError:
            break
    print("")
    return num_of_elem

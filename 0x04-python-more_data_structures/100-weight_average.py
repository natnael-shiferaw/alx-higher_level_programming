#!/usr/bin/python3


def weight_average(my_list=[]):

    if not my_list:
        return 0

    NUM = 0
    DEN = 0

    for T in my_list:
        NUM += T[0] * T[1]
        DEN += T[1]

    return (NUM / DEN)

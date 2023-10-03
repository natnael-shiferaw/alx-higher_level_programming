#!/usr/bin/python3


def print_last_digit(number):
    if number < 0:
        num_last = (-number % 10)
    elif number >= 0:
        num_last = number % 10
    print("{:d}".format(num_last), end="")
    return num_last

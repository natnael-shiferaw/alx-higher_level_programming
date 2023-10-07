#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """This program is used to print matrix of integers."""
    for ROW in matrix:
        for COL in row:
            print("{:d}".format(COL), end=" " if COL != ROW[-1] else "")
        print()

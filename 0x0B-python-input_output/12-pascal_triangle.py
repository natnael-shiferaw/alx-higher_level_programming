#!/usr/bin/python3

"""This Python file is used to Define
a function for Pascal's Triangle."""


def pascal_triangle(n):
    """A function that is used to represent
    Pascal's Triangle with size of n.

    Returns a LIST of LISTS of integers
    that represents the triangle.
    """

    if n <= 0:
        return []

    Triangle = [[1]]

    while len(Triangle) != n:
        t = Triangle[-1]
        temp = [1]

        for k in range(len(t) - 1):
            temp.append(t[k] + t[k + 1])
        temp.append(1)
        Triangle.append(temp)

    return Triangle

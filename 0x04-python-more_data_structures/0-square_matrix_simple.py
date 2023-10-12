#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    New_matrix = matrix.copy()

    for n in range(len(matrix)):
        New_matrix[n] = list(map(lambda x: x**2, matrix[n]))

    return (New_matrix)

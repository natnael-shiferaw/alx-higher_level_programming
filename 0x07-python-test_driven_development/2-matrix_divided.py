#!/usr/bin/python3
"""THIS PYTHON FILE DEFINES A MATRIX DIVISION FUNCTION."""


def matrix_divided(matrix, div):

    """A FUNCTION USED TO DIVIDE EVERY ELEMENT IN THE MATRIX.

    Args:
        matrix (list): IT'S A LIST OF LISTS THAT CONTAIN INT'S/FLOAT'S.
        div (int/float): REPRESENTS A DIVISIOR.
    Raises:
        TypeError: IT THE MATRIX CONTAIN ANYTHING OTHER THAN NUMBERS.
        TypeError: IF IT CONTAINS ROWS THAT ARE DIFFERENT SIZE.
        TypeError: IF div ISN'T FLOAT/INT.
        ZeroDivisionError: FINALLY IF div IS ZERO.
    Returns:
        RETRUNS A NEW MATRIX FOR THE DIVISION RESULT.
    """

    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(ELEM, int) or isinstance(ELEM, float))
                for ELEM in [NUM for row in matrix for NUM in row])):

        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):

        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):

        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])

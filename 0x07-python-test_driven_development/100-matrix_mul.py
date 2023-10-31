#!/usr/bin/python3
"""THIS PYTHON FILE DEFINES A FUNCTION THAT IS USED FOR THE
MULTIPLICATION OF MATRICES, SPECIFICALLY IN THIS CASE TWO MATRICES."""


def matrix_mul(m_a, m_b):
    """A FUNCTION USED FOR MULTIPLYING TWO MATRICES.

    Args:
        m_a (list of lists of ints/floats): REPRESENTS THE FIRST MATRIX.
        m_b (list of lists of ints/floats): THIS REPRESENTS THE SECOND MATRIX.
    Raises:
        TypeError: IF ONE OF THE MATRICES IS EMPTY.
        TypeError: IF ONE OF THEM HAS DIFFERENT-SIZED ROWS.
        TypeError: IF ONE OF THE MATRICES IS NOT A LIST OF LISTS OF INT/FLOAT.
        ValueError: IF THE TWO MATRICES CAN'T BE MULTIPLIED.
    Returns:
        RETURNS A NEW MATRIX THAT REPRESENTS THE
        MULTIPLICATION OF THE TWO MATRICES.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ELEM, int) or isinstance(ELEM, float))
               for ELEM in [NUM for row in m_a for NUM in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ELEM, int) or isinstance(ELEM, float))
               for ELEM in [NUM for row in m_b for NUM in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_b_INVERTED = []

    for r in range(len(m_b[0])):
        newROW = []
        for n in range(len(m_b)):
            newROW.append(m_b[n][r])
        m_b_INVERTED.append(newROW)

    newMATRIX = []
    for row in m_a:
        newROW = []

        for col in m_b_INVERTED:
            PRODU = 0

            for k in range(len(m_b_INVERTED[0])):
                PRODU += row[k] * col[k]
            newROW.append(PRODU)

        newMATRIX.append(newROW)

    return newMATRIX

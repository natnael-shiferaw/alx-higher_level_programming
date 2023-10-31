#!/usr/bin/python3
"""A PYTHON FILE THAT IS USED TO DEFINE A FUNCTION THAT PERFOMRS
A MARTIX MULTIPLICATION BY USING NumPy."""

import numpy as nmpy


def lazy_matrix_mul(m_a, m_b):
    """A FUNCTION THAT IS USED TO RETURN MULTIPLICATION OF 2 MATRICES.

    Args:
        m_a (list of lists of ints/floats): REPRESENTS THE FIRST MATRIX.
        m_b (list of lists of ints/floats): REPRESENTS THE SECOND MATRIX.
    """

    return (nmpy.matmul(m_a, m_b))

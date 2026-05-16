#!/usr/bin/env python3
"""
this module returns the addition, subtraction, multiplication, and division
of two numpy.ndarray matrices
"""


def np_elementwise(mat1, mat2):
    """
    returns the addition, subtraction, multiplication, and division
    of two numpy.ndarray matrices
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)

#!/usr/bin/env python3
"""
    concatenates two matrices along a specific axis.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    mat1: list of lists of ints/floats
    mat2: list of lists of ints/floats
    axis: axis to concatenate
    """
    if axis == 0:
        if len(mat1[0]) == len(mat2[0]):
            return mat1 + mat2
    elif axis == 1:
        if len(mat1) == len(mat2):
            return [mat1[i] + mat2[i] for i in range(len(mat1))]
    else:
        return None

#!/usr/bin/env python3
"""
    performs matrix multiplication.
"""


def mat_mul(mat1, mat2):
    """
    mat1: list of lists of ints/floats
    mat2: list of lists of ints/floats
    """
    if len(mat1[0]) == len(mat2):
        return [
            [
                sum(a * b for a, b in zip(row, col))
                for col in zip(*mat2)
            ]
            for row in mat1
        ]
    else:
        return None

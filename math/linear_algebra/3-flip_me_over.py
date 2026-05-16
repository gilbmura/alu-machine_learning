#!/usr/bin/env python3
"""
    flips a 2D matrix over its main diagonal.
"""


def matrix_transpose(matrix):
    """
    matrix: matrix to be transposed
    """
    trans_matrix = [[matrix[j][i] for j in range(len(matrix))]
                    for i in range(len(matrix[0]))]
    return trans_matrix

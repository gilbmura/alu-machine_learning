#!/usr/bin/env python3
"""
This module contains the functions to calculate
the correlation between two variables.
"""


import numpy as np


def correlation(C):
    """
    This function calculates the correlation matrix
    for a dataset.

    Arguments:
     - C: a numpy.ndarray of shape (d, d) containing
          the covariance matrix of the data.
    - d: the number of dimensions.

    Returns:
     A numpy.ndarray of shape (d, d) containing the
        correlation matrix.
    """
    if type(C) is not np.ndarray:
        raise TypeError("C must be a numpy.ndarray")
    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    d = C.shape[0]
    corr_matrix = np.zeros_like(C, dtype=float)

    for i in range(d):
        for j in range(d):
            var_i = np.sqrt(C[i, i])
            var_j = np.sqrt(C[j, j])

            if var_i != 0 and var_j != 0:
                corr_matrix[i, j] = C[i, j] / (var_i * var_j)
            elif var_i == 0 and var_j == 0:
                corr_matrix[i, j] = 0
            else:
                corr_matrix[i, j] = np.nan
    return corr_matrix

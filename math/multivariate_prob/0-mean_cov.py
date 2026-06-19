#!/usr/bin/env python3
"""
This module contains the function to calculate the mean
and covariance of a multivariate distribution.
"""


import numpy as np


def mean_cov(X):
    """
    args:
    - X: numpy.ndarray (d, n) containing the data set:
        - d: number of dimensions
        - n: number of data points

    returns:
    mean, cov:
    - mean: numpy.ndarray (d, 1) containing the mean of the data set
    - cov: numpy.ndarray (d, d) containing the covariance matrix of
    the data set
    """
    if type(X) is not np.ndarray or len(X.shape) != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    if X.shape[0] < 2:
        raise ValueError('X must contain multiple data points')

    n, d = X.shape
    mean = np.mean(X, axis=0, keepdims=True)
    center_data = X - mean
    len_data = X.shape[0] - 1
    cov = np.dot(center_data.T, center_data) / len_data
    return mean, cov

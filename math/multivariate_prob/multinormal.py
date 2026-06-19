#!/usr/bin/env python3
"""
This module contains a class that represents a Multivariate
Normal distribution.
"""


import numpy as np


class MultiNormal:
    """
    This class represents a Multivariate Normal distribution.
    where:
    - data: a numpy.ndarray of shape (d, n) containing the data set.
    - n: the number of data points.
    - d: the number of dimensions in each data point.
    - mean: a numpy.ndarray of shape (d, 1) containing the mean of data.
    - cov: a numpy.ndarray of shape (d, d) containing the covariance
    matrix data.
    """
    def __init__(self, data):
        """
        This method initializes the MultiNormal class.
        """
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        if data.shape[1] < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)
        diff = data - self.mean
        self.cov = np.dot(diff, diff.T) / (data.shape[1] - 1)

    def pdf(self, x):
        """
        This method calculates the PDF at a data point.
        """
        if type(x) is not np.ndarray:
            raise TypeError("x must be a numpy.ndarray")
        d = self.cov.shape[0]
        if len(x.shape) != 2:
            raise ValueError("x must have the shape ({}, 1)".format(d))
        check_d, one = x.shape
        if check_d != d or one != 1:
            raise ValueError("x must have the shape ({}, 1)".format(d))

        det = np.linalg.det(self.cov)
        inv = np.linalg.inv(self.cov)
        pdf = 1.0 / np.sqrt(((2 * np.pi) ** d) * det)
        mult = np.matmul(np.matmul((x - self.mean).T, inv), (x - self.mean))
        pdf *= np.exp(-0.5 * mult)
        pdf = pdf[0][0]
        return pdf

#!/usr/bin/env python3

"""
poisson distribution
"""


class Poisson():
    """
    poisson distribution
    """
    def __init__(self, data=None, lambtha=1.):
        """
        data is a list of the data to be used to estimate the distribution
        lambtha is the expected number of occurences in a given interval
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)

        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of “successes”.
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        e = 2.7182818285
        factorial = 1
        for i in range(1, k + 1):
            factorial *= i
        return ((e ** (-self.lambtha)) * (self.lambtha ** k)) / factorial

    def cdf(self, k):
        """
        Calculates the value of the CDF for a given number of “successes”.
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        e = 2.7182818285
        summation = 0
        for i in range(k + 1):
            factorial = 1
            for j in range(1, i + 1):
                factorial *= j
            summation += (self.lambtha ** i) / factorial
        return (e ** (-self.lambtha)) * summation

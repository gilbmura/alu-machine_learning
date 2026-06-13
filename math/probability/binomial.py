#!/usr/bin/env python3
"""
binomial distribution
"""


class Binomial():
    """
    binomial distribution
    """
    def __init__(self, data=None, n=1, p=0.5):
        """
        class constructor
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if not 0 < p < 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)

        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = float(sum(data) / len(data))
            summation = 0
            for i in data:
                summation += (i - mean) ** 2
            variance = (summation / len(data))
            self.p = 1 - (variance / mean)
            self.n = round(mean / self.p)
            self.p = float(mean / self.n)

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of “successes”
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        factorial_n = 1
        factorial_k = 1
        factorial_nk = 1
        for i in range(1, self.n + 1):
            factorial_n *= i
        for i in range(1, k + 1):
            factorial_k *= i
        for i in range(1, self.n - k + 1):
            factorial_nk *= i
        return ((factorial_n / (factorial_k * factorial_nk)) *
                (self.p ** k) * ((1 - self.p) ** (self.n - k)))

    def cdf(self, k):
        """
        calculates the value of the CDF for a given number of “successes”
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        summation = 0
        for i in range(k + 1):
            summation += self.pmf(i)
        return summation

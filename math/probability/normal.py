#!/usr/bin/env python3
"""
normal distribution
"""


class Normal():
    """
    normal distribution
    """
    def __init__(self, data=None, mean=0., stddev=1.):
        """
        data is a list of the data to be used to estimate the distribution
        mean is the mean of the distribution
        stddev is the standard deviation of the distribution
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.stddev = float(stddev)
            self.mean = float(mean)

        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            summation = 0
            for i in data:
                summation += (i - self.mean) ** 2
            self.stddev = (summation / len(data)) ** 0.5

    def z_score(self, x):
        """
        Calculates the z-score of a given x-value
        """
        return ((x - self.mean) / self.stddev)

    def x_value(self, z):
        """
        Calculates the x-score of a given z-value
        """
        return ((z * self.stddev) + self.mean)

    def pdf(self, x):
        """
        Calculates the value of the PDF for a given x-value
        """
        e = 2.7182818285
        pi = 3.1415926536
        return ((1 / (self.stddev * ((2 * pi) ** 0.5))) *
                (e ** (-0.5 * (((x - self.mean) / self.stddev) ** 2))))

    def cdf(self, x):
        """
        Calculates the value of the CDF for a given x-value
        """
        e = 2.7182818285
        pi = 3.1415926536
        value = (x - self.mean) / (self.stddev * (2 ** (1 / 2)))
        val = value - ((value ** 3) / 3) + ((value ** 5) / 10)
        val = val - ((value ** 7) / 42) + ((value ** 9) / 216)
        val *= (2 / (pi ** (1 / 2)))
        cdf = (1 / 2) * (1 + val)
        return cdf

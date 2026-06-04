#!/usr/bin/env python3
"""
returns the coefficients of the integral of a polynomial
"""


def poly_integral(poly, C=0):
    """
    if poly or C not valid return None
    """
    if not isinstance(poly, list) or len(poly) < 1 or not isinstance(C, int):
        return None
    for i in poly:
        if type(i) is not int and type(i) is not float:
            return None
    if type(C) is float and C.is_integer():
        C = int(C)
    integral = [C]
    for power, coefficient in enumerate(poly):
        if (coefficient % (power + 1)) is 0:
            new_coefficient = coefficient // (power + 1)
        else:
            new_coefficient = coefficient / (power + 1)
        integral.append(new_coefficient)
    while integral[-1] is 0 and len(integral) > 1:
        integral = integral[:-1]
    return integral

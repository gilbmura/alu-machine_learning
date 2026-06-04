#!/usr/bin/env python3
"""
returns the coefficients of the derivative of a polynomial
"""


def poly_derivative(poly):
    """
    if poly not valid return None, and
    if derivative is 0 return [0]
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    elif len(poly) <= 1:
        return [0]
    deriv_poly = [poly[i] * i for i in range(1, len(poly))]
    return deriv_poly

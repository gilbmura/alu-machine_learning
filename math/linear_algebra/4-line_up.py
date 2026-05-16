#!/usr/bin/env python3
"""
    adds two arrays element-wise.
"""


def add_arrays(arr1, arr2):
    """
    arr1: list of ints/floats
    arr2: list of ints/floats
    """
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]

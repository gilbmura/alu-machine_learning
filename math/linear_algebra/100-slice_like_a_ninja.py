#!/usr/bin/env python3
'''
    A function def np_slice(matrix, axes):
    that slices matrix along axes
'''


def np_slice(matrix, axes):
    '''
        A function def np_slice(matrix, axes):
        that slices matrix along axes
    '''
    slices_matrix = [slice(None)] * len(matrix.shape)

    for axis, value in axes.items():
        slices_matrix[axis] = slice(*value)

    return matrix[tuple(slices_matrix)]

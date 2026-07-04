#!/usr/bin/env python3
"""
Function to perform a same convolution on grayscale images
"""
import numpy as np


def convolve_grayscale_same(images, kernel):
    """
    Function to perform a same convolution on grayscale images
    Args:
        images: numpy.ndarray with shape (m, h, w) containing multiple
                grayscale images
                m is the number of images
                h is the height in pixels of the images
                w is the width in pixels of the images
        kernel: numpy.ndarray with shape (kh, kw) containing the kernel
                for the convolution
                kh is the height of the kernel
                kw is the width of the kernel
    Returns: numpy.ndarray containing the convolved images
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    ph = max(int((kh - 1) / 2), int(kh / 2))
    pw = max(int((kw - 1) / 2), int(kw / 2))
    padded = np.pad(images, ((0, 0), (ph, ph), (pw, pw)), 'constant')
    conv = np.zeros((m, h, w))
    for i in range(h):
        for j in range(w):
            image = padded[:, i:i+kh, j:j+kw]
            conv[:, i, j] = np.sum(image * kernel, axis=(1, 2))
    return conv

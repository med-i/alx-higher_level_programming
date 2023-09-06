#!/usr/bin/python3
"""
Module to multiply 2 matrices using numpy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function to multiply two matrices using numpy's matmul method.

    Args:
        m_a: list of lists of integers/floats.
        m_b: list of lists of integers/floats.

    Returns:
        New matrix with the product.
    """
    return np.matmul(m_a, m_b)

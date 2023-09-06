#!/usr/bin/python3
"""
This module is designed for multiplying 2 matrices.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The product of m_a and m_b.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or not any(m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or not any(m_b):
        raise ValueError("m_b can't be empty")

    if not all(isinstance(x, (int, float)) for row in m_a for x in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(x, (int, float)) for row in m_b for x in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for row in m_a:
        new_row = []
        for j in range(len(m_b[0])):
            new_row.append(sum(row[i] * m_b[i][j] for i in range(len(row))))
        result.append(new_row)

    return result

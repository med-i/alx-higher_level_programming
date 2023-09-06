#!/usr/bin/python3
"""
Module designed for dividing matrix elements by a given divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides matrix elements by a divisor,
    rounding results to 2 decimal places.

    Args:
        matrix (list of lists of int/float):
            Matrix with numbers to be divided.
        div (int, float): The divisor.

    Returns:
        list of lists of float: New matrix with divided elements.

    Raises:
        TypeError: If matrix format is incorrect, rows have different sizes,
                   or the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(error_msg)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(error_msg)

    row_length = len(matrix[0])
    for row in matrix[1:]:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        if not (
            all(isinstance(x, (int, float)) for x in row)
            or len(row) != row_length
        ):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]

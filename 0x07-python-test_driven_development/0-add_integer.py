#!/usr/bin/python3
"""
Module designed for adding two numbers together.
"""


def add_integer(a, b=98):
    """
    Computes the sum of two numbers after converting them to integers.

    Args:
        a (int, float): The first operand.
        b (int, float, optional): The second operand. Defaults to 98.

    Returns:
        int: The addition result of a and b.

    Raises:
        TypeError: If either a or b is neither an integer nor a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    try:
        return int(a) + int(b)
    except:
        raise OverflowError("Float overflow")

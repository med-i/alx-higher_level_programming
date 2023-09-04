#!/usr/bin/python3
"""Module to add two integers.
"""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int or float): The first integer.
        b (int or float): The second integer (defaults to 98).

    Returns:
        int: The result of adding a and b.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

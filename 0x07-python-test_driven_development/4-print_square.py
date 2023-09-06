#!/usr/bin/python3
"""
Module designed to print a square using the character '#'.
"""


def print_square(size):
    """
    Prints a square using the '#' character.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer or if it's a float less than 0.
        ValueError: If size is less than 0.
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

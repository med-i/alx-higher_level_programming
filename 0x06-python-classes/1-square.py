#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Class that defines a square by: (based on 0-square.py).

    Attributes:
        __size: The size of the square.
    """

    def __init__(self, size):
        """Instantiation with size.

        Args:
            size (no type/value verification).
        """
        self.__size = size

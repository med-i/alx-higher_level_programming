#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Class that defines a square by: (based on 1-square.py).

    Attributes:
        __size(int): The size of the square.
    """

    def __init__(self, size=0):
        """Instantiate the Square with size."

        Args:
            size(int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

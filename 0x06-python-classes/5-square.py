#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Class that defines a square by: (based on 4-square.py).

    Attributes:
        __size(int): The size of the square.
    """

    def __init__(self, size=0):
        """Instantiate the Square with size.

        Args:
            size(int, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: the area of the square."""
        return self.__size**2

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
        for _ in range(self.__size):
            print("#" * self.__size)

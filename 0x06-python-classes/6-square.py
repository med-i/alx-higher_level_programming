#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Defines a square with a specific size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square with a size and a position.

        Args:
            size (int, optional): The size of the square's side. Defaults to 0.
            position (tuple, optional): A tuple of two integers representing the position. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square's side.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): A tuple of two integers representing the position.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character #, considering its position."""
        if self.__size == 0:
            print()
        for _ in range(self.position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.position[0] + "#" * self.__size)

#!/usr/bin/python3
"""Simple base geometry module.

classes:
    BaseGeometry: A simple geometry class.
"""


class BaseGeometry:
    "Base geometry class."

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the valuer.

        Args:
            name (str): The name of the integer.
            value (int): The integer to validates.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

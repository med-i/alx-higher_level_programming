#!/usr/bin/python3
"""
This module defines the Base class.
"""


class Base:
    """Represents the base class for other shapes.

    Attributes:
        id (int, optional): The id for the shape.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance with
        a given id or auto-incremented one.

        Args:
            id (int, optional): The id of the shape.
                                Defaults to auto-incremented.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

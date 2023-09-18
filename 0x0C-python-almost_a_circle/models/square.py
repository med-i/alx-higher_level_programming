#!/usr/bin/python3
"""
This module defines the Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square.

    Attributes:
        size (int): Size of the square side.
        x (int): The horizontal coordinate of the square.
        y (int): The vertical coordinate of the square.
        id (int): The unique id of the square.

    Inherits from:
        Rectangle: The parent class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
            x (int): The horizontal coordinate of the square. Defaults to 0.
            y (int): The vertical coordinate of the square. Defaults to 0.
            id (int, optional): The unique id of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square side.

        Args:
            value (int): The value to set the size to.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square's attributes.

        Args:
            args (tuple): No-keyword argument.
            kwargs (dict): Key-worded argument.
        """
        attributes = ["id", "size", "x", "y"]
        if args:
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Get the dictionary representation of the square.

        Returns:
            dict: The dictionary representation of the square.
        """
        return {"id": self.id, "x": self.x, "size": self.width, "y": self.y}

    def __str__(self):
        """Override the '__str__' method.

        Returns:
            str: The string representation of the square.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

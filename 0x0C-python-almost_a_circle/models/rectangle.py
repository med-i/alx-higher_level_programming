#!/usr/bin/python3
"""
This module defines the Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The horizontal coordinate of the rectangle.
        __y (int): The vertical coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The horizontal coordinate of the rectangle. Defaults to 0.
            y (int): The vertical coordinate of the rectangle. Defaults to 0.
            id (int, optional): The id of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If 'value' is not an int.
            ValueError: If 'value' is under or equals to 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If 'value' is not an int.
            ValueError: If 'value' is under or equals to 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: Get the horizontal coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the horizontal coordinate of the rectangle.

        Args:
            value (int): The horizontal coordinate of the rectangle.

        Raises:
            TypeError: If 'value' is not an int.
            ValueError: If 'value' is under 0.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: Get the vertical coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the vertical coordinate of the rectangle.

        Args:
            value (int): The vertical coordinate of the rectangle.

        Raises:
            TypeError: If 'value' is not an int.
            ValueError: If 'value' is under 0.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """Print the rectangle with the charater '#' to the stdout."""
        col_space = "\n" * self.y
        row_space = " " * self.x
        row = row_space + "#" * self.width
        print(col_space + "\n".join([row] * self.height))

    def update(self, *args, **kwargs):
        """Update the rectangle's attributes.

        Args:
            args (tuple): No-keyword argument.
            kwargs (dict): Key-worded argument.
        """
        attributes = ["id", "width", "height", "x", "y"]
        if args:
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Get the dictionary representation of the rectangle.

        Returns:
            dict: The dictionary representation of the rectangle.
        """
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width,
        }

    def __str__(self):
        """Override the '__str__' method.

        Returns:
            str: The string representation of the rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

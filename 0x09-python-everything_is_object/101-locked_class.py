#!/usr/bin/python3
"""This module contains a class that restricts the creation
of dynamic attributes.
"""


class LockedClass:
    """A class that restricts dynamic attribute creation.

    Attributes:
        first_name (str): The first name for class instances.
    """

    __slots__ = ["first_name"]

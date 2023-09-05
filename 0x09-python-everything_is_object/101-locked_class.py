#!/usr/bin/python3
"""This module contains a class that restricts the creation
of dynamic attributes.
"""


class LockedClass:
    """_summary_

    Attributes:
        first_name (str): The first name for class instances.
    """

    __slots__ = ["first_name"]

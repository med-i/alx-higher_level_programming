#!/usr/bin/python3
"""Checks the exact type of an object."""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance
    of the specified class.

    Args:
        obj (object): The object to check.
        a_class(class): The class to compare the object to.

    Returns:
        boolean: True if obj is exactly an instance of the a_class."""
    return type(obj) is a_class

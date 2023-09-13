#!/usr/bin/python3
"""Checks the type of an object."""


def is_kind_of_class(obj, a_class):
    """Returns true if the object is an instance of the specified class.

    Args:
        obj (object): The object to check.
        a_class(class): The class to compare the object to.

    Returns:
        boolean: True if obj is an instance of the a_class."""
    return isinstance(obj, a_class)

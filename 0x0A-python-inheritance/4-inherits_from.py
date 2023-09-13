#!/usr/bin/python3
"""Checks if the object is an instance of a class."""


def inherits_from(obj, a_class):
    """Returns true if the object is an instance of a class that inherited
    from the specified class.

    Args:
        obj (object): The object to check.
        a_class(class): The class to compare the object to.

    Returns:
        boolean: True if obj is an instance of the a_class
        and not type of the a_class."""
    return type(obj) is not a_class and isinstance(obj, a_class)

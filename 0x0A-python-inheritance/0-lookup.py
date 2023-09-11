#!/usr/bin/python3
"""Inspects the object attributes and methods.
"""


def lookup(obj):
    """
    Returns attributes and methods of the given object.

    Args:
        obj (object): Object to inspect.

    Returns:
        list: Attributes and methods of the object.
    """
    return dir(obj)

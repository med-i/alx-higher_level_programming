#!/usr/bin/python3
"""
Handles the indentation of a given text.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters:
    ., ? and :.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join([line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")

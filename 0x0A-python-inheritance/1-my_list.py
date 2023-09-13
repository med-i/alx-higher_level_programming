#!/usr/bin/python3
"""
Demonstrates a custom list with a method to print sorted elements.

Classes:
    MyList: Inherits from list and adds a method to print sorted elements.
"""


class MyList(list):
    """
    A custom list with an added method to print sorted elements.

    Attributes:
        Inherited from the built-in list class.

    Methods:
        print_sorted: Prints the elements of the list in sorted order.
    """

    def print_sorted(self):
        """Prints the elements of the list in sorted order."""
        sorted_list = sorted(self)
        print(sorted_list)

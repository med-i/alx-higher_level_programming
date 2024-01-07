#!/usr/bin/python3
"""
This module define the find_peak method
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    if size == 2:
        return max(list_of_integers[0], list_of_integers[1])

    for i in range(1, size - 1):
        previous = list_of_integers[i-1]
        current = list_of_integers[i]
        next = list_of_integers[i+1]
        if current >= previous and current >= next:
            return current

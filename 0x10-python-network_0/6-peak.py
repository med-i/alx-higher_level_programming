#!/usr/bin/python3
"""
This module define the find_peak method
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    size = len(list_of_integers)
    if size == 0:
        return None

    peak = list_of_integers[0]
    for i in range(size):
        if list_of_integers[i] > peak:
            peak = list_of_integers[i]

    return peak

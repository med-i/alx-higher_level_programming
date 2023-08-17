#!/usr/bin/python3


def roman_to_int(roman_string):
    roman_numerals = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
    }

    int = 0
    for c in roman_string:
        int += roman_numerals[c]

    return int

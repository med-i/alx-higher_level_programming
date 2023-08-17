#!/usr/bin/python3


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    subtractives = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    integer = 0
    i = 0
    while i < len(roman_string):
        sub = roman_string[i : i + 2]
        if sub in subtractives:
            integer += subtractives[sub]
            i += 2
        else:
            integer += numerals.get(roman_string[i], 0)
            i += 1

    return integer

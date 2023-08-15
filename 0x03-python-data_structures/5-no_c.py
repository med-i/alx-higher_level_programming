#!/usr/bin/python3


def no_c(my_string):
    new_string = ""
    for idx, char in enumerate(my_string):
        if char not in ["c", "C"]:
            new_string += char

    return new_string

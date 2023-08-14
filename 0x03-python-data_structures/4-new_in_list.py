#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    new_list = list(my_list)

    if idx in range(0, len(new_list)):
        new_list[idx] = element

    return new_list

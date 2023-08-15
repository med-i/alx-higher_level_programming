#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return

    reversed_list = list(my_list)
    reversed_list.reverse()

    for i in reversed_list:
        print("{:d}".format(i))

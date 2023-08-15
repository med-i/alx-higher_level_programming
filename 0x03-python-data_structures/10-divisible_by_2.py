#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    multiples_of_two = []

    for num in my_list:
        multiples_of_two.append(True if num % 2 == 0 else False)

    return multiples_of_two

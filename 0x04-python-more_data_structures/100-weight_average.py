#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0

    mul = 0
    div = 0
    for tuple in my_list:
        mul += tuple[0] * tuple[1]
        div += tuple[1]

    return 0 if div == 0 else mul / div


my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))

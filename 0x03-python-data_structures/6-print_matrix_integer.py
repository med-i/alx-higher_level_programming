#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in range(len(row)):
            end = " " if col < len(row) - 1 else ""
            print("{:d}".format(row[col]), end=end)
        print()

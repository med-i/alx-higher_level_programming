#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda lst: list(map(lambda num: num**2, lst)), matrix))

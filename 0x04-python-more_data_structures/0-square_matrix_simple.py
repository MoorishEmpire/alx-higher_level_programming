#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    size = len(matrix)
    if size == 0:
        return []
    new_matrix = [[0] * len(matrix[i]) for i in range(size)]
    for i in range(size):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = matrix[i][j] ** 2
    return new_matrix

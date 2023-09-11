#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if my_list is None:
        my_list = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            if (j != 0):
                print(" ", end='')
            print("{:d}".format(matrix[i][j]), end='')
        print()

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        q = 1
        for j in i:
            if q == len(i):
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
            q = q + 1
        print()

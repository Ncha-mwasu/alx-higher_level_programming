#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lists in matrix:
        for rows in lists:
            if rows == lists[(len(lists) - 1)]:
                print("{:d}".format(rows), end="")
            else:
                print("{:d}".format(rows), end=" ")
        print()

#!/usr/bin/python3
"""
A matrix division module
"""


def matrix_divided(matrix, div):
    """This function takes two inputs(a matrix and div(int/float))
    and divides the matrix by div.
    Args:
        matrix: a matrix of numbers(int/float) - 1st argument
    div: a number - 2nd argument

    Return:
        a new matrix with the results of the division of the old matrix

    Raises:
        TypeError: if matrix is not of int/float type
                    and if the lengths of the nested matrices are not equal
                    if div is also not of int/float type
        ZeroDivisionError: if div is 0
    """
    msg_size = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_size)

    if not isinstance(div, int) and not isinstance (div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for item in matrix:
        if not item or not isinstance(item, list):
            raise TypeError(msg_size)

        if len(matrix[0]) != len(item):
            raise TypeError("Each row of the matrix must have the same size")

        for num in item:
            if not isinstance(num, int) and not isinstance (num, float):
                raise TypeError(msg_size)

    return ([list(map(lambda x: round(x / div, 2), i))for i in matrix])

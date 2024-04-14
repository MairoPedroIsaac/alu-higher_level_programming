#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Args:
        matrix : A list of lists of ints or floats.
        div: must be a number(integer or float).
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix containing the result of the division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
=======
def matrix_divided(matrix, div):
    """
    Returns: a new matrix 
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_mat = [[0] * len(matrix[0]) for x in range(len(matrix))]
    row_len = len(matrix[0])
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[i]) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            output = (matrix[i][j]) / div
            new_mat[i][j] = round(output, 2)
    return new_mat
>>>>>>> f898bcdda45c8c870540e004dcde26c456cd29d6

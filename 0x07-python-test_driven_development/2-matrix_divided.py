#!/usr/bin/python3
"""A function matrix_divided(matrix, div) is defined"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
    - matrix (list of lists): A matrix containing integers or floats.
    - div (int or float): The divisor.

    Returns:
    - list of lists: New matrix with elements divided by 'div',
      rounded to 2 decimal places.

    Raises:
    - TypeError: If the input is not a list of lists of integers or floats,
      or if the divisor is not a number.
    - TypeError: If each row of the matrix does not have the same size.
    - ZeroDivisionError: If the divisor is zero.
    """

    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or not all(
        isinstance(val, (int, float)) for row in matrix for val in row
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number and not equal to zero
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and round to 2 decimal places
    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]

    return new_matrix

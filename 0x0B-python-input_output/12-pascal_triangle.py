#!/usr/bin/python3
"""A function is defined."""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.

    Args:
    - n (int): Number of rows for Pascal's triangle.

    Returns:
    - list: List of lists of integers representing Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)  # Initialize the row with 1s
        if i >= 2:
            # Calculate the values for the inner elements of the row
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

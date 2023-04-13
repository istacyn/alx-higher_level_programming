#!/usr/bin/python3
"""This module creates the Pascal's triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the
    Pascal’s triangle of n.

    Args:
    n (int): The number of rows in the Pascal's triangle.

    Returns:
    A list of n lists where each list represents
    a row of the Pascal's triangle.
    An empty list if n <= 0.
    """
    if n <= 0:
        return []

    # Create first row
    triangle = [[1]]

    # Create reamining rows
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)

        triangle.append(row)

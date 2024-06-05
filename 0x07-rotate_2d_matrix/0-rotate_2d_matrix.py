#!/usr/bin/python3
"""
Module Rotates 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    This rotates a 2D matrix 90 degrees clockwise.
    """
    x = len(matrix)

    # Transpose the matrix
    for i in range(0, x):
        for j in range(i + 1, x):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp

    for i in range(x):
        matrix[i].reverse()

#!/usr/bin/python3
""" Pascal triagle function """


def pascal_triangle(n):
    """ This evaluates the pascal triangle 
    args: n(integer)
    return: a list of lists of integer
    """

    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1]

        for j in range(i + 1):
            if (j == 0 or j == i):
                row.append(1)
            else:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])

        triangle.append(row)

    return triangle

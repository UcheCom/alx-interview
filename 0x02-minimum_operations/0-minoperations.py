#!/usr/bin/python3
"""Module performs minimum operations"""


def minOperations(n):
    """calculates the fewest number of operations
    needed to result in exactly n H characters in the file

    Arg:
       n: integer.
    Returns: an integer, if n is impossible to achieve, return 0.
    """
    if n == 1:
        return 0

    ops = 0
    min_ops = 2

    while n > 1:
        while n % min_ops == 0:
            ops += min_ops
            n /= min_ops
        min_ops += 1
    return ops

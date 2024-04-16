#!/usr/bin/python3
"""Module solves N queens problem"""
import sys

if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def safe_queens(n, i=0, x=[], y=[], z=[]):
    """Function finds every solution to the problem
      args:
        @n:the size of the chess board/N queens on NxN board
        @i:the current row being considered/starts from the 1st row
        @x, y & z: lists track the positions of the queens on
         board.
    """
    if i < n:
        for j in range(n):
            if j not in x and i + j not in y and i - j not in z:
                yield from safe_queens(n, i + 1, x + [j],
                                       y + [i + j], z + [i - j])
    else:
        yield x


def solve_queens(n):
    """This solves N quenns"""
    m = []
    i = 0
    for solution in safe_queens(n, 0):
        for s in solution:
            m.append([i, s])
            i += 1
        print(m)
        m = []
        i = 0


solve_queens(n)

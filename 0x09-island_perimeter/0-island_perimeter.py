#!/usr/bin/python3
'''Module defines Island perimeter'''


def island_perimeter(grid):
    '''This returns the Perimeter of an island in the grid'''

    rows = len(grid)
    cols = len(grid[0])

    p = 0
    cons = 0

    for x in range(0, rows):
        for y in range(0, cols):
            if grid[x][y] == 1:
                p += 4

                if x != 0 and grid[x - 1][y]:
                    cons += 1
                if y != 0 and grid[x][y - 1]:
                    cons += 1
    return p - (cons * 2)

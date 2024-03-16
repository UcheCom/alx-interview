#!/usr/bin/python3
"""Method that determines if all boxes can be opened"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked
    Arg:
       boxes: list of lists
    Return:
       True or False
    """
    x = len(boxes)
    seen = set()
    seen.add(0)  # First box opened

    keys = [0]

    while keys:
        curr_box = keys.pop()
        for key in boxes[curr_box]:
            if key < x and key not in seen:
                seen.add(key)
                keys.append(key)
    return len(seen) == x

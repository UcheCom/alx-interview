#!/usr/bin/python3
"""Coin Change"""


def makeChange(coins, total):
    """
    This returns the minimum number of coins needed to meet a given total
    Args:
        coins (ints): a list of coins of different values
        total (int): total value to be calculated
    Return:
        Number of coins or -1 if meeting the total is impossible
    """
    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if total == 0:
            break
        q = total // coin
        count += q
        total -= q*coin

    if total != 0:
        return -1
    return count

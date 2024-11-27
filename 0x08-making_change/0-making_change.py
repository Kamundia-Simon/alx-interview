#!/usr/bin/python3
"""Coin Changer using dynamic programming"""


def makeChange(coins, total):
    """
    determine the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0

    dyn_loop = [float('inf')] * (total + 1)
    dyn_loop[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            if dyn_loop[i - coin] != float('inf'):
                dyn_loop[i] = min(dyn_loop[i], dyn_loop[i - coin] + 1)

    return dyn_loop[total] if dyn_loop[total] != float('inf') else -1

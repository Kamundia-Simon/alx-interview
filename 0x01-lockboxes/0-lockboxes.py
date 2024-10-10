#!/usr/bin/python3
"""function determining boxes unlocked in a list of lists"""


def canUnlockAll(boxes):
    """
    Args:
        boxes ([int]): list of lists of integers.

    Returns: True if unlocked otherwise False

    """
    opened = [False] * len(boxes)
    opened[0] = True
    keys = [0]

    while keys:
        current = keys.pop()
        for key in boxes[current]:
            if key < len(boxes) and not opened[key]:
                opened[key] = True
                keys.append(key)
    return all(opened)

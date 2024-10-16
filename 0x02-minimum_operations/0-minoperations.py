#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """alculates the fewest number of operations
    needed to result in exactly n H characters"""
    if n <= 1:
        return 0
    operations = 0
    divide = 2
    while n > 1:
        while n % divide == 0:
            operations += divide
            n //= divide
        divide += 1
    return operations

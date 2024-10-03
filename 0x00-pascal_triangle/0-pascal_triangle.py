#!/usr/bin/python3
"""
function  that returns a list of lists of integers representing the Pascal’s triangle of n
"""
def pascal_triangle(n):
    if n <= 0:
        return []
    tri = []
    for i in range(n):
        row = [1] * (i + 1)

        for j in range(1, i):
             row[j] = tri[i - 1][j - 1] + tri[i - 1][j]

        tri.append(row)
    return tri

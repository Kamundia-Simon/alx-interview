#!/usr/bin/python3
"""N Queens puzzle solution using backtracking"""
import sys


def print_solutions(solutions):
    """Prints all solutions"""
    for solution in solutions:
        print(solution)


def is_safe(board, row, col):
    """Checks if a queen can be placed on board"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_queens(n, row=0, board=[], solutions=[]):
    """Uses backtracking to solve the N queens problem"""
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            solve_queens(n, row + 1, board, solutions)
            board.pop()


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_queens(n, 0, [], solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    main()

#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col].
    """
    # Check the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check the diagonals
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve_nqueens(N, row, board, solutions):
    """
    solve the N queens problem by trying to place a queen in each row.
    """
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)
            board[row] = -1


def main():
    """
    handle input validation and initiate the N queens solution process.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []

    solve_nqueens(N, 0, board, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()

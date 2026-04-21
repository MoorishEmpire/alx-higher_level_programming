#!/usr/bin/python3
"""Program solves the N queens puzzle.'"""
import sys


def main():
    argc = len(sys.argv)
    if argc != 2:
        print("Usage: nqueens N")
        exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)

    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        exit(1)

    board = [-1] * N
    backTrack(board, 0, N)


def backTrack(board, row, n):
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return

    col = 0
    while (col < n):
        if is_safe(board, row, col):
            board[row] = col
            backTrack(board, row + 1, n)
            board[row] = -1
        col += 1


def is_safe(board, row, col):
    i = 0
    while (i < row):
        row_diff = row - i
        col_diff = col - board[i]
        if col == board[i] or abs(row_diff) == abs(col_diff):
            return False
        i += 1
    return True


if __name__ == "__main__":
    main()

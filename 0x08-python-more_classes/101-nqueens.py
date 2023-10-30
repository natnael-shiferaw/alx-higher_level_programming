#!/usr/bin/python3
"""THIS FILE IS USED TO SOLVE THE nqueens puzzle."""

import sys


def BOARD_INIT(n):
    """A FUNCTION THAT INITIALIZES an `n`x`n` sized CHESSBOARD WITH 0'S."""
    
    CHESS_BOARD = []
    [CHESS_BOARD.append([]) for k in range(n)]
    [row.append(' ') for i in range(n) for row in CHESS_BOARD]

    return CHESS_BOARD


def DEEPCPY_BOARD(CHESS_BOARD):
    """A FUCNTION THAT RETURNS a deepcopy of a CHESSBOARD."""

    if isinstance(CHESS_BOARD, list):
        return list(map(DEEPCPY_BOARD, CHESS_BOARD))
    return CHESS_BOARD


def GETsolution(CHESS_BOARD):
    """A FUCNTION THAT RETURNS LIST OF LISTS OF
	REPRESENTATION OF SOLVED CHESSBOARD."""

    SOL = []
    for K in range(len(CHESS_BOARD)):

        for H in range(len(CHESS_BOARD)):
            if CHESS_BOARD[K][H] == "Q":
                SOL.append([K, H])
                break
    return SOL


def X_OUT(CHESS_BOARD, row, col):
    """X OUTSPOSTS THE CHESSBOARD.

    Args:
        CHESS_BOARD (list): CURRENT CHESSBOARD.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    
    for J in range(col + 1, len(CHESS_BOARD)):
    
        CHESS_BOARD[row][J] = "x"

    for J in range(col - 1, -1, -1):
        CHESS_BOARD[row][J] = "x"

    for Z in range(row + 1, len(CHESS_BOARD)):
        CHESS_BOARD[Z][col] = "x"

    for Z in range(row - 1, -1, -1):
        CHESS_BOARD[Z][col] = "x"

    J = col + 1

    for Z in range(row + 1, len(CHESS_BOARD)):
        if J >= len(CHESS_BOARD):
            break
        CHESS_BOARD[Z][J] = "x"
        J += 1

    J = col - 1

    for Z in range(row - 1, -1, -1):
        if J < 0:
            break
        CHESS_BOARD[Z][J]
        J -= 1

    J = col + 1
    for Z in range(row - 1, -1, -1):
        if J >= len(CHESS_BOARD):
            break
        CHESS_BOARD[Z][J] = "x"
        J += 1

    J = col - 1
    for Z in range(row + 1, len(CHESS_BOARD)):
        if J < 0:
            break
        CHESS_BOARD[Z][J] = "x"
        J -= 1


def SOLVE_RECURSION(CHESS_BOARD, row, queens, SOLN):
    """FUCNTION SOLVE N-QUEENS PUZZLE RECURSIVELY.

    Args:
        CHESS_BOARD (list): CURRENT CHESSBOARD.
        row (int): CURRENT ROW.
        queens (int): The current number of placed queens.
        SOLN (list): A list of lists of solutions.
    Returns:
        SOLN
    """
    if queens == len(CHESS_BOARD):
        SOLN.append(GETsolution(CHESS_BOARD))
        return SOLN

    for L in range(len(CHESS_BOARD)):

        if CHESS_BOARD[row][L] == " ":

            TEMP_BOARD = DEEPCPY_BOARD(CHESS_BOARD)
            TEMP_BOARD[row][L] = "Q"
            X_OUT(TEMP_BOARD, row, L)
            SOLN = SOLVE_RECURSION(TEMP_BOARD, row + 1,
                                        queens + 1, SOLN)

    return SOLN


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    BOARD = BOARD_INIT(int(sys.argv[1]))
    SOLUTION = SOLVE_RECURSION(BOARD, 0, 0, [])

    for SOL in SOLUTION:
        print(SOL)

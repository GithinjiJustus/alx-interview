#!/usr/bin/python3
import sys

def print_solution(board):
    """Print the solution in the required format"""
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)

def is_safe(board, row, col):
    """Check if a queen can be placed on board[row][col]"""
    # Check the current column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the upper-right diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(board, row):
    """Solve the N Queens problem using backtracking"""
    if row == len(board):
        print_solution(board)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, row + 1)
            board[row][col] = 0  # Backtrack

def main():
    """Main function to handle input and start solving the N Queens problem"""
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

    # Initialize the chessboard
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0)

if __name__ == "__main__":
    main()

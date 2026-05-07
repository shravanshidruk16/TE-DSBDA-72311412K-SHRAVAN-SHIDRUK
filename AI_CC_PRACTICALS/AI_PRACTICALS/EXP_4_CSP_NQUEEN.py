# N-Queens Problem using Backtracking

"""
Time Complexity

Worst Case:

O(N!) : Because many possible arrangements are checked.

Space Complexity

O(N**2) : Due to chessboard storage.
"""

N = 4

# Create empty chessboard
board = [[0] * N for _ in range(N)]


# Function to check safe position
def is_safe(row, col):

    # Check left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal
    i, j = row, col

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i, j = row, col

    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


# Backtracking function
def solve(col):

    # All queens placed
    if col >= N:
        return True

    # Try every row
    for row in range(N):

        if is_safe(row, col):

            # Place queen
            board[row][col] = 1

            # Recursive call
            if solve(col + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Main Program
if solve(0):

    print("Solution Found:\n")

    for row in board:
        print(row)

else:
    print("No Solution")
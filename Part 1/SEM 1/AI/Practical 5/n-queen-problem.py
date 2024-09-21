def is_safe(board, row, col):
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check lower diagonal on the left
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, col):
    if col >= len(board):
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens(board, col + 1):
                return True
            board[i][col] = 0
    return False

def n_queens(n):
    board = [[0] * n for _ in range(n)]
    if not solve_n_queens(board, 0):
        print("No solution found.")
        return
    for row in board:
        print(" ".join(["Q" if cell == 1 else "." for cell in row]))
if __name__ == "__main__":
    n = 8  # Change this to the desired board size
    n_queens(n)
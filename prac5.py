
def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


def is_safe(board, row, col, n):
    # Check the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_nqueens(board, row + 1, n):
                return True

            board[row][col] = 0

    return False


n = int(input("Enter the value of N: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    board = [[0] * n for _ in range(n)]

    if solve_nqueens(board, 0, n):
        print("\nN-Queens Matrix:")
        print_board(board, n)
    else:
        print("No solution exists for N =", n)

def dfs_n_queens(n):
    if n < 1:
        return []

    board = [-1] * n
    solutions = []

    def is_safe(row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(list(board))
            return

        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)

    backtrack(0)
    return solutions

# print(f"n=1: {dfs_n_queens(1)}")     
# print(f"n=2: {dfs_n_queens(2)}")     
# print(f"n=3: {dfs_n_queens(3)}")     
print(f"n=4: {dfs_n_queens(4)}")     
print(f"n=8 (len): {len(dfs_n_queens(8))}") 
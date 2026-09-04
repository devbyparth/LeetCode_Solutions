class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [['.' for _ in range(n)] for _ in range(n)]

        def is_safe(row, col):
            # Check column above
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # Check upper-left diagonal
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # Check upper-right diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def backtrack(row):
            # Base case: placed queens on all N rows -> found 1 valid solution
            if row == n:
                return 1

            count = 0
            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = 'Q'
                    count += backtrack(row + 1)  # Accumulate solutions from deeper branches
                    board[row][col] = '.'        # Backtrack step

            return count

        return backtrack(0)
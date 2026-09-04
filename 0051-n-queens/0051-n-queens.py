class Solution:
    def is_safe(self, board, row, col, n):
        # Check column above current row
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

    def nQueens(self, board, row, n, ans):
        if row == n:
            ans.append(["".join(r) for r in board])
            return

        for j in range(n):
            if self.is_safe(board, row, j, n):
                board[row][j] = 'Q'
                self.nQueens(board, row + 1, n, ans)
                board[row][j] = '.'

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.nQueens(board, 0, n, ans)
        return ans
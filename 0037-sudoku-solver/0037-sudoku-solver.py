class Solution:
    def is_safe(self, board, row, col, digit):
        # Horizontal check
        if digit in board[row]:
            return False
        
        # Vertical
        for r in range(9):
            if board[r][col] == digit:
                return False

        # Small Box
        gridRow = (row // 3) * 3
        gridCol = (col // 3) * 3
        for r in range(gridRow, gridRow + 3):
            for c in range(gridCol, gridCol + 3):
                if board[r][c] == digit:
                    return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        digits = list('123456798')
        
        def bactrack(board, row, col):
            if row == 9:
                return True
            
            nextRow = row+1 if col+1 == 9 else row
            nextCol = 0 if col+1 == 9 else col+1
            
            
            if board[row][col] != '.':
                return bactrack(board, nextRow, nextCol)
            
            for dig in digits:
                if self.is_safe(board, row, col, dig):
                    board[row][col] = dig
                    if bactrack(board, nextRow, nextCol):
                        return True
                    board[row][col] = '.'

            return False

        bactrack(board, 0, 0)
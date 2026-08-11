class Solution(object):
    def isValidSudoku(self, board):
        n = len(board)

        rowSet = [set() for _ in range(n)]
        colSet = [set() for _ in range(n)]
        boxSet = [set() for _ in range(n)]

        for r in range(n):
            for c in range(n):
                val = board[r][c]

                if val == '.':
                    continue

                boxIndex = (r//3) * 3 + (c // 3)

                if val in rowSet[r] or val in colSet[c] or val in boxSet[boxIndex]:
                    return False

                rowSet[r].add(val)
                colSet[c].add(val)
                boxSet[boxIndex].add(val)

        return True
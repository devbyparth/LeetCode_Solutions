class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diag = set()  # (row + col)
        neg_diag = set()  # (row - col)

        ans = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r: int):
            if r == n:
                ans.append(["".join(row) for row in board])
                return

            for c in range(n):
                # O(1) checks using math properties
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                # Add state
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                # Recurse for next row
                backtrack(r + 1)

                # Backtrack state
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return ans
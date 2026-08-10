class Solution(object):
    def equalPairs(self, grid):
        n = len(grid)
        pairs = 0
        rows = {}
        for row in grid:
            rows[tuple(row)] = rows.get(tuple(row), 0) + 1

        for col in range(n):
            column = tuple(grid[r][col] for r in range(n))

            if column in rows:
                pairs += rows[column]

        return pairs
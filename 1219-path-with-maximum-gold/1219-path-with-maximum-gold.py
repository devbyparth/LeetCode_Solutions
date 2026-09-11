class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            
            gold = grid[r][c]
            grid[r][c] = 0          # mark visited (in-place, no extra set needed)
            
            best = 0
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                best = max(best, dfs(r + dr, c + dc))
            
            grid[r][c] = gold       # backtrack — restore for other starting points
            return gold + best
        
        max_gold = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    max_gold = max(max_gold, dfs(r, c))
        
        return max_gold
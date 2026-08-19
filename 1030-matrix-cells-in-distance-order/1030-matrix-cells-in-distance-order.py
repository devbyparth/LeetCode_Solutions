class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        max_dist = (rows - 1) + (cols - 1)
        bucket = [[] for _ in range(max_dist+1)]

        for r in range (rows):
            for c in range(cols):
                dist = abs(r - rCenter) + abs(c - cCenter)
                bucket[dist].append([r, c])
        res = []
        
        for group in bucket:
            res.extend(group)
        
        return res
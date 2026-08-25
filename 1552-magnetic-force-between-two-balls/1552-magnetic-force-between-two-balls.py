class Solution(object):
    def maxDistance(self, position, m):
        position.sort()

        def canPlace(d):
            count = 1
            last_pos = position[0]

            for i in range(1, len(position)):
                if position[i] - last_pos >= d:
                    count += 1
                    last_pos = position[i]
                    if count == m:
                        return True
            return False
        
        low, high = 1, position[-1] - position[0]
        ans = 1
        while low <= high:
            mid = (low + high) // 2

            if canPlace(mid):
                ans = mid       # 'mid' is feasible, try to maximize distance
                low = mid + 1
            else:
                high = mid - 1  # 'mid' is too large, search smaller distances

        return ans
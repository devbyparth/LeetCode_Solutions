import math
class Solution(object):
    def minimizedMaximum(self, n, quantities):
        def canDistribute(x):
            stores_needed = sum(math.ceil(q / x) for q in quantities)
            return stores_needed <= n
        
        low, high = 1, max(quantities)
        ans = high
        while low <= high:
            mid = (low + high) // 2

            if canDistribute(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
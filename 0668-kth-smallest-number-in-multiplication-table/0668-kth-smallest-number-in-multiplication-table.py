class Solution(object):
    def findKthNumber(self, m, n, k):
        def count_len(x):
            # How many entries in m*n table are <= x
            total = 0
            for row in range(1, m+1):
                total += min(x//row, n)
            return total
        
        low, high = 1, m*n

        while low < high:
            mid = (low + high) // 2
            if count_len(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low
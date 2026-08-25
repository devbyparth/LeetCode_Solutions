class Solution(object):
    def findBestValue(self, arr, target):
        low, high = 0, max(arr)
        ans, min_diff = float('inf'), float('inf')
        
        while low <= high:
            mid = (low + high) // 2

            # Calculate sum where elements > mid are capped at mid
            cur_sum = sum(mid if n > mid else n for n in arr)
            diff = abs(cur_sum - target)

            if diff < min_diff:
                min_diff = diff
                ans = mid
            elif diff == min_diff:
                ans = min(ans, mid)
            
            if cur_sum < target:
                low = mid + 1
            elif cur_sum > target:
                high = mid - 1
            else:
                return mid
        return ans
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        low, high = 1, max(nums)
        ans = 1
        while low <= high:
            mid = (low + high) // 2
            
            cur_sum = 0
            for n in nums:
                adder = (n // mid) if n % mid == 0 else (n // mid) + 1
                cur_sum += adder
            
            if cur_sum <= threshold:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
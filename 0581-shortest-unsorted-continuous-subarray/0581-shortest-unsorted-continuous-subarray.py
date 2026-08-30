class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        left, right = -1, -2
        min_seen = nums[-1]
        max_seen = nums[0]
        
        for i in range(1, n):
            # Track maximum moving left-to-right to find the right boundary
            max_seen = max(max_seen, nums[i])
            if nums[i] < max_seen:
                right = i
            
            # Track minimum moving right-to-left to find the left boundary
            min_seen = min(min_seen, nums[n - 1 - i])
            if nums[n - 1 - i] > min_seen:
                left = n - 1 - i
                
        return right - left + 1
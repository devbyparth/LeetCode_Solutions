class Solution(object):
    def splitArray(self, nums, k):
        low, high = max(nums), sum(nums)
        
        while low < high:
            mid = (low + high) // 2
            
            # Count required subarrays for max sum cap of 'mid'
            subarrays = 1
            current_sum = 0
            
            for num in nums:
                if current_sum + num > mid:
                    subarrays += 1
                    current_sum = num
                else:
                    current_sum += num
            
            # Binary search logic
            if subarrays <= k:
                high = mid      # Try a smaller max sum
            else:
                low = mid + 1   # Max sum 'mid' was too small
                
        return low
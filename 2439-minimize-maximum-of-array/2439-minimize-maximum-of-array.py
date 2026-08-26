class Solution(object):
    def minimizeArrayValue(self, nums):
        ans = 0
        prefix_sum = 0
        
        for i, num in enumerate(nums):
            prefix_sum += num
            # Pure integer ceiling division: ceil(prefix_sum / (i + 1))
            current_avg = (prefix_sum + i) // (i + 1)
            ans = max(ans, current_avg)
            
        return ans
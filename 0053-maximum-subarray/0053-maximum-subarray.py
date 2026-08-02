class Solution(object):
    def maxSubArray(self, nums):
        
        cur_sum = max_sum = float('-inf')

        for i in nums:
            cur_sum = max(cur_sum + i, i)
            max_sum = max(max_sum, cur_sum)

        return max_sum
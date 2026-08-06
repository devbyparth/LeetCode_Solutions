class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)

        curr_sum = sum(nums)
        desired_sum = (n * (n + 1)) // 2

        return desired_sum - curr_sum
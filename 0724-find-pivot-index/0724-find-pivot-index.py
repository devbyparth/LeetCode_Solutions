class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            if leftSum == total - leftSum - nums[i]:
                return i
            leftSum += nums[i]

        return -1
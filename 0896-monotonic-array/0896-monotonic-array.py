class Solution(object):
    def isMonotonic(self, nums):
        i = 0
        while i+1 < len(nums) and nums[i] <= nums[i+1]:
            i += 1

        if i == len(nums)-1:
            return True

        i = len(nums)-1
        while i-1 >= 0 and nums[i-1] >= nums[i]:
            i -= 1

        if i == 0:
            return True

        return False
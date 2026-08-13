class Solution(object):
    def buildArray(self, nums):

        for i in range(len(nums)):
            nums[i] = len(nums) * (nums[nums[i]] % len(nums)) + nums[i]

        for j in range(len(nums)):
            nums[j] = nums[j] // len(nums)

        return nums
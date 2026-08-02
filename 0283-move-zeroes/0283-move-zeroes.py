class Solution(object):
    def moveZeroes(self, nums):
        insert = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[insert] = nums[insert], nums[i]
                insert += 1

        return nums
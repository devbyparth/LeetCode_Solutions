class Solution(object):
    def findDuplicates(self, nums):
        result = []

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
            else:
                result.append(abs(nums[i]))

        return result
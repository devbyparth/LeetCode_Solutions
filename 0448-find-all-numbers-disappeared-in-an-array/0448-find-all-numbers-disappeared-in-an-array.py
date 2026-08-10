class Solution(object):
    def findDisappearedNumbers(self, nums):
        if not nums:
            return []

        result = []

        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        for index, num in enumerate(nums):
            if num > 0:
                result.append(index + 1)

        return result
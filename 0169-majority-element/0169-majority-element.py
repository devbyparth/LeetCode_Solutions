class Solution(object):
    def majorityElement(self, nums):

        candidate = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if count < 1:
                candidate = nums[i]
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1

        return candidate
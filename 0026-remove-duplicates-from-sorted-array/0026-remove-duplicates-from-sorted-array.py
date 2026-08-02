class Solution(object):
    def removeDuplicates(self, nums):
        left = 0
        right = 1

        while right < len(nums):
            if nums[right] == nums[left]:
                right = right + 1
            else:
                left += 1
                nums[left] = nums[right]

        return left+1
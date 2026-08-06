class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        curr_count = 0

        for num in nums:
            if num == 1:
                curr_count += 1
                max_count = max(max_count, curr_count)

            if num != 1:
                curr_count = 0
                max_count = max(max_count, curr_count)

        return max_count
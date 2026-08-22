class Solution(object):
    def longestSubarray(self, nums):
        if len(nums) == sum(nums):
            return len(nums) - 1
        left, zero_count, max_len = 0, 0, 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            cur_len = right - left
            max_len = max(max_len, cur_len)
        return max_len
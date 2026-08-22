class Solution(object):
    def longestOnes(self, nums, k):
        left, right, max_len, cur_len = 0, 0, 0, 0
        count = 0

        while right < len(nums):
            if nums[right] == 0:
                count += 1

            while count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1

            cur_len = right - left + 1
            max_len = max(max_len, cur_len)
            right += 1

        return max_len
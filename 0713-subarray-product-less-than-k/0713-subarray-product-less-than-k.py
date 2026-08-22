class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        result = 0
        left, right = 0, 0

        cur_product = 1

        while right < len(nums):
            cur_product *= nums[right]

            while cur_product >= k:
                cur_product //= nums[left]
                left += 1

            result += right - left + 1
            right += 1
        return result
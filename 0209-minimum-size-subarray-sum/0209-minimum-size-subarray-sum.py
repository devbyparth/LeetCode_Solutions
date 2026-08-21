class Solution(object):
    def minSubArrayLen(self, target, nums):
        min_length = float('inf')
        window_sum = 0
        left = 0

        for right, num in enumerate(nums):
            # expand: absorb nums[right] into the window
            window_sum += num

            # contract: while window already meets target, try to shrink from the left
            while window_sum >= target:
                min_length = min(min_length, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return 0 if min_length == float('inf') else min_length
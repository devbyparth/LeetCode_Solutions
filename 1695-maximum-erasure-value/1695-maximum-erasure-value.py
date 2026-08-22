from collections import defaultdict
class Solution(object):
    def maximumUniqueSubarray(self, nums):
        max_sum = float('-inf')
        window_arr = defaultdict(int)

        left, right = 0, 0
        cur_sum = 0

        while right < len(nums):
            incoming = nums[right]
            cur_sum += incoming

            window_arr[incoming] += 1

            while len(window_arr) < (right - left + 1):
                outgoing = nums[left]
                left += 1
                cur_sum -= outgoing
                window_arr[outgoing] -= 1
                if window_arr[outgoing] == 0:
                    del window_arr[outgoing]
            right += 1
            max_sum = max(max_sum, cur_sum)
        return max_sum
from collections import defaultdict
class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def atMost(k_val):
            windowMap = defaultdict(int)
            left, right, count = 0, 0, 0

            while right < len(nums):
                incoming = nums[right]
                windowMap[incoming] += 1

                while len(windowMap) > k_val:
                    outgoing = nums[left]
                    windowMap[outgoing] -= 1
                    if windowMap[outgoing] == 0:
                        del windowMap[outgoing]
                    left += 1

                count += right - left + 1
                right += 1
            return count

        return atMost(k) - atMost(k - 1)
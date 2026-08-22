class Solution(object):
    def minOperations(self, nums, x):
        target = sum(nums) - x
        
        # Exact sum x requires picking all elements
        if target == 0:
            return len(nums)
        # Impossible to reach x
        if target < 0:
            return -1

        left = 0
        current_sum = 0
        max_len = -1

        for right in range(len(nums)):
            current_sum += nums[right]

            # Shrink window if current_sum exceeds target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1

            # Valid middle window found
            if current_sum == target:
                max_len = max(max_len, right - left + 1)

        return len(nums) - max_len if max_len != -1 else -1
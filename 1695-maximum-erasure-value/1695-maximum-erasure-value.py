class Solution(object):
    def maximumUniqueSubarray(self, nums):
        seen = set()

        left, cur_sum, max_sum = 0, 0, 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                cur_sum -= nums[left]
                left += 1
            
            seen.add(nums[right])
            cur_sum += nums[right]
            max_sum = max(max_sum, cur_sum)
        
        return max_sum
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_right = []
        max_till_now = float('-inf')
        for num in reversed(nums):
            max_till_now = max(max_till_now, num)
            max_right.append(max_till_now)
        max_right = max_right[::-1]
        res = 0
        left = 0
        for right in range(len(nums)):
            while nums[left] > max_right[right]:
                left += 1
            res = max(res, right - left)
        
        return res
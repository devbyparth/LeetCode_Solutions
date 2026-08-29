class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n, res = len(nums), 0
        
        # 1. Sum of Subarray Minimums
        stack = []
        for i, val in enumerate(nums + [float('-inf')]):
            while stack and (i == n or nums[stack[-1]] > val):
                j = stack.pop()
                left = j - stack[-1] if stack else j + 1
                right = i - j
                res -= nums[j] * left * right
            stack.append(i)
            
        # 2. Sum of Subarray Maximums
        stack = []
        for i, val in enumerate(nums + [float('inf')]):
            while stack and (i == n or nums[stack[-1]] < val):
                j = stack.pop()
                left = j - stack[-1] if stack else j + 1
                right = i - j
                res += nums[j] * left * right
            stack.append(i)
            
        return res
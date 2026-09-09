from functools import cache

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        @cache
        def backtrack(index: int, remain: int) -> int:
            # Base Case: All numbers must be assigned a sign
            if index == len(nums):
                return 1 if remain == 0 else 0

            # Option 1: Assign '+' to nums[index] -> subtract from remaining target
            plus = backtrack(index + 1, remain - nums[index])

            # Option 2: Assign '-' to nums[index] -> add back to remaining target
            minus = backtrack(index + 1, remain + nums[index])

            return plus + minus

        return backtrack(0, target)
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        i = nums.index(min(nums))
        j = nums.index(max(nums))
        left, right = min(i, j), max(i, j)

        # remove everything from right
        op1 = right + 1

        # remove everything from left
        op2 = n-left

        # remove 'left' from front, 'right' from back
        op3 = (left + 1) + (n - right)

        return min(op1, op2, op3)
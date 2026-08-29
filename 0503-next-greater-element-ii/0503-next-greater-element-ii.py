class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []  # Stores indices of elements

        # Loop twice to simulate circular array traversal
        for i in range(2 * n - 1, -1, -1):
            curr_idx = i % n

            while stack and nums[stack[-1]] <= nums[curr_idx]:
                stack.pop()

            res[curr_idx] = nums[stack[-1]] if stack else -1

            stack.append(curr_idx)

        return res
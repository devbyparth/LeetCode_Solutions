class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = []
        third = float('-inf')  # Tracks nums[k] (the '2' in the 132 pattern)

        # Iterate right-to-left to process candidates for nums[j] and nums[k]
        for num in reversed(nums):
            # If current number < third, we found nums[i] < nums[k] < nums[j]
            if num < third:
                return True
            
            # Maintain a monotonic decreasing stack
            # Any element popped by 'num' can serve as a valid 'third' (nums[k])
            while stack and stack[-1] < num:
                third = stack.pop()
            
            stack.append(num)

        return False
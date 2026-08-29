class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n  # Default right boundary is 'n', not -1
        stack = []

        # Right Smaller (Iterate backwards)
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = n if not stack else stack[-1]
            stack.append(i)

        stack.clear()

        # Left Smaller (Iterate forwards)
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = -1 if not stack else stack[-1]
            stack.append(i)  # Added missing append

        ans = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            cur_area = heights[i] * width
            ans = max(ans, cur_area)
            
        return ans
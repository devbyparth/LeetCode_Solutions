from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        # Helper function: LeetCode 84 (Largest Rectangle in Histogram)
        def largestRectangleArea(heights: List[int]) -> int:
            stack = []
            max_h_area = 0
            h_copy = heights + [0]  # Sentinel element to flush remaining stack elements

            for i, h in enumerate(h_copy):
                while stack and h_copy[stack[-1]] > h:
                    height = h_copy[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_h_area = max(max_h_area, height * width)
                stack.append(i)

            return max_h_area

        # Convert each row into a cumulative histogram bar array
        for row in matrix:
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            max_area = max(max_area, largestRectangleArea(heights))

        return max_area
class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # Check if X-intervals overlap AND Y-intervals overlap
        return (
            rec1[0] < rec2[2] and  # rec1's left is to the left of rec2's right
            rec2[0] < rec1[2] and  # rec2's left is to the left of rec1's right
            rec1[1] < rec2[3] and  # rec1's bottom is below rec2's top
            rec2[1] < rec1[3]      # rec2's bottom is below rec1's top
        )
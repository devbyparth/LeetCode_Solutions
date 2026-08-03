class Solution(object):
    def maxProduct(self, nums):

        first, second = float('-inf'), float('inf')

        for num in nums:
            if num > first:
                first, second = num, first

            elif num > second:
                second = num

        return (first - 1) * (second - 1)
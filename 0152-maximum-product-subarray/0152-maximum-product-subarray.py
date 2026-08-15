class Solution(object):
    def maxProduct(self, nums):
        n = len(nums)
        maxProduct = float('-inf')
        leftProduct = 1
        rightProduct = 1

        for i in range(n):
            leftProduct = leftProduct * nums[i]
            rightProduct = rightProduct * nums[n - i - 1]
            
            maxProduct = max(maxProduct, leftProduct, rightProduct)
            
            if leftProduct == 0:
                leftProduct = 1
            if rightProduct == 0:
                rightProduct = 1
        
        return maxProduct
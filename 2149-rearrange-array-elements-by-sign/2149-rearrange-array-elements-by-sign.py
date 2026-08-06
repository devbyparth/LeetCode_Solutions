class Solution(object):
    def rearrangeArray(self, nums):
        result = [0] * len(nums)

        pos = 0
        neg = 1
        for i in nums:
            if i > 0:
                result[pos] = i
                pos += 2
            else:
                result[neg] = i
                neg += 2
        
        return result
class Solution(object):
    def sumOfUnique(self, nums):
        freqMap = {}
        sum = 0
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        
        for k, v in freqMap.items():
            if v == 1:
                sum += k
        
        return sum
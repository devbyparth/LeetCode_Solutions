class Solution(object):
    def numIdenticalPairs(self, nums):

        hashMap = {}

        count = 0

        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1

        for value in hashMap.values():
            count = count + (value * (value - 1) // 2)

        return count
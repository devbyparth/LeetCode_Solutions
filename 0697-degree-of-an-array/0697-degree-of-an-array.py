class Solution(object):
    def findShortestSubArray(self, nums):
        first, last, count = {}, {}, {}

        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            count[num] = count.get(num, 0) + 1

        degree = max(count.values())

        minLen = float('inf')
        for nums in count:
            if count[nums] == degree:
                minLen = min(minLen, last[nums]-first[nums]+1)
        
        return minLen
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        countMap = {}

        for i in nums1:
            for j in nums2:
                countMap[i+j] = countMap.get(i+j, 0) + 1
        count = 0
        for i in nums3:
            for j in nums4:
                count += countMap.get(-(i+j), 0)
        
        return count
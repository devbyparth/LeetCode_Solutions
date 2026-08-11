from collections import Counter

class Solution(object):
    def sort_key(self, x):
        return (self.countMap[x], -x)

    def frequencySort(self, nums):
        self.countMap = Counter(nums)
        return sorted(nums, key=self.sort_key)
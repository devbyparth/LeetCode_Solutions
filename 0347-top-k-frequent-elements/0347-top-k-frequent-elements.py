from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        result = []
        frequency = Counter(nums)

        for key, val in frequency.most_common(k):
            result.append(key)

        return result
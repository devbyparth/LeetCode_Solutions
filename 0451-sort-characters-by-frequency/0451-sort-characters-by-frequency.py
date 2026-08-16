from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        freqCount = Counter(s)
        result = []
        for k, v in freqCount.most_common():
            for _ in range(v):
                result.append(k)
        return ''.join(result)
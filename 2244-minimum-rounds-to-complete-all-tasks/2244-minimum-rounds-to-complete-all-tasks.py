from collections import Counter
from math import ceil


class Solution(object):
    def minimumRounds(self, tasks):
        freqMap = Counter(tasks)

        rounds = 0

        for v in freqMap.values():
            if v == 1:
                return -1
            if v % 3 == 0:
                rounds += v // 3
            else:
                rounds += (v // 3) + 1
        return rounds

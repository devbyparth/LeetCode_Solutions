from collections import Counter

class Solution(object):
    def minimumRounds(self, tasks):
        freqMap = Counter(tasks)

        rounds = 0

        for v in freqMap.values():
            if v == 1:
                return -1
            rounds += -(-v // 3)

        return rounds

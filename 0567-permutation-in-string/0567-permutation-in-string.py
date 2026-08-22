from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s2) < len(s1):
            return False

        checkMap = Counter(s1)
        windowMap = Counter(s2[:len(s1)])

        if checkMap == windowMap:
            return True

        for i in range(len(s1), len(s2)):
            income_char = s2[i]
            out_char = s2[i - len(s1)]

            windowMap[income_char] += 1
            windowMap[out_char] -= 1

            if windowMap[out_char] == 0:
                del windowMap[out_char]

            if windowMap == checkMap:
                return True
        return False
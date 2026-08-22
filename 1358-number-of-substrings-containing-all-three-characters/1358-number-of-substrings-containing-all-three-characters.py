from collections import defaultdict
class Solution(object):
    def numberOfSubstrings(self, s):
        def atMost(k_val):
            checkMap = defaultdict(int)
            left, right, count, = 0, 0, 0

            while right < len(s):
                incoming = s[right]
                checkMap[incoming] += 1

                while len(checkMap) > k_val:
                    outgoing = s[left]
                    checkMap[outgoing] -= 1
                    if checkMap[outgoing] == 0:
                        del checkMap[outgoing]
                    left += 1

                count += right - left + 1
                right += 1
            return count

        return atMost(3) - atMost(2)
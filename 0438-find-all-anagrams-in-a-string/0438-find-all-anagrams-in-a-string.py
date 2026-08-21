from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        idx_list = []
        pMap = Counter(p)
        sMap = Counter(s[:len(p)])

        for i in range(len(s) - len(p) + 1):
            if pMap == sMap:
                idx_list.append(i)
            
            if i + len(p) < len(s):
                incoming_char = s[i + len(p)]
                outgoing_char = s[i]

                sMap[incoming_char] += 1
                sMap[outgoing_char] -= 1
                if sMap[outgoing_char] == 0:
                    del sMap[outgoing_char]
        
        return idx_list
from collections import Counter
class Solution(object):
    def countGoodSubstrings(self, s):
        if len(s) < 3:
            return 0
        
        k = 3
        window_count = Counter(s[:k])
        count = 1 if len(window_count) == k else 0

        for i in range(k, len(s)):
            left_char = s[i-k]
            new_char = s[i]

            window_count[new_char] = window_count.get(new_char, 0) + 1

            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
            
            if len(window_count) == k:
                count += 1
        return count

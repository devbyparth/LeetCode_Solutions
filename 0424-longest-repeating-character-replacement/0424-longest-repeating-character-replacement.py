class Solution(object):
    def characterReplacement(self, s, k):
        left, right, max_len, max_freq = 0, 0, 0, 0
        char_map = {}

        while right < len(s):
            char_map[s[right]] = char_map.get(s[right], 0) + 1
            max_freq = max(max_freq, char_map[s[right]])

            while (right - left + 1) - max_freq > k:
                char_map[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
            right += 1
        
        return max_len
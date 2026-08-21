class Solution(object):
    def longestSubstring(self, s, k):
        # base cases: empty string, or string too short to ever satisfy k
        if len(s) == 0 or len(s) < k:
            return 0

        # count frequency of every character in the current piece
        char_counts = {}
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1

        # find the first character that appears fewer than k times —
        # no valid answer can ever contain this character, so it's a valid split point
        for i, char in enumerate(s):
            if char_counts[char] < k:
                # split the string on this character and solve each side independently,
                # then take the best of the two halves
                left_part = s[:i]
                right_part = s[i+1:]
                return max(self.longestSubstring(left_part, k), self.longestSubstring(right_part, k))

        # no character violated the k-requirement — the entire current piece is valid
        return len(s)
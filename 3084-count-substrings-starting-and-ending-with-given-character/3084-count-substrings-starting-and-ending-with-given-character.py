class Solution(object):
    def countSubstrings(self, s, c):

        count = 0
        sub_count = 0

        for i in range(len(s)):
            if s[i] == c:
                sub_count += 1 + count
                count += 1

        return sub_count
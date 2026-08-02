class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        s_chars = list(s)
        t_chars = list(t)

        s_counts = {}
        t_counts = {}
        for i in range(len(s_chars)):
            s_counts[s_chars[i]] = s_counts.get(s_chars[i], 0) + 1
            t_counts[t_chars[i]] = t_counts.get(t_chars[i], 0) + 1

        for key in s_counts.keys():
            if s_counts[key] != t_counts.get(key, 0):
                return False

        return True
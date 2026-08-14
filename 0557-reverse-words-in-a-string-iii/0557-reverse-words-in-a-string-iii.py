class Solution(object):
    def reverseWords(self, s):
        s = s.split()
        res = []

        for word in s:
            res.append(word[::-1])

        return (' '.join(res)).strip()
class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        res = [''] * len(s)

        for word in s:
            pos = int(word[-1]) - 1

            res[pos] = word[:-1]
        
        return ' '.join(res)
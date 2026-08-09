class Solution(object):
    def groupAnagrams(self, strs):
        res = {}
        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)

            if key not in res:
                res[key] = []
            res[key].append(word)

        return list(res.values())
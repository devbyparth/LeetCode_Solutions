class Solution(object):
    def commonChars(self, words):

        result = []
        fMap = {}
        for char in words[0]:
            fMap[char] = fMap.get(char, 0) + 1

        for i in range(1, len(words)):
            currMap = {}
            for char in words[i]:
                currMap[char] = currMap.get(char, 0) + 1
            for char in fMap:
                fMap[char] = min(fMap[char], currMap.get(char, 0))

        for k, v in fMap.items():
            if v>0:
                for _ in range(v):
                    result.append(str(k))

        return result
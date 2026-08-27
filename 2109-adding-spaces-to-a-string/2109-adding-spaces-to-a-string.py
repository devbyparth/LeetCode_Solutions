class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        space = 0
        n_spaces = len(spaces)

        for i, char in enumerate(s):
            if space < n_spaces and i == spaces[space]:
                res.append(' ')
                space += 1
            res.append(char)
        
        return ''.join(res)
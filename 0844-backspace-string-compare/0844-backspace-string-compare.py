class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1, s2 = [], []

        for char in s[:]:
            if char == '#' and s1:
                s1.pop()
            elif char != "#":
                s1.append(char)
        
        for char in t[:]:
            if char == '#' and s2:
                s2.pop()
            elif char != "#":
                s2.append(char)
        
        return s1 == s2
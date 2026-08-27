class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seen = set()
        repeated = set()
        
        for i in range(len(s) - 9):
            ten_letter = s[i : i + 10]
            if ten_letter in seen:
                repeated.add(ten_letter)
            else:
                seen.add(ten_letter)
                
        return list(repeated)
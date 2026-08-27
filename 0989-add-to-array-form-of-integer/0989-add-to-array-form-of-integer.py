class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        i = len(num) - 1
        res = []
        
        # Process digits from right to left, adding k to each position
        while i >= 0 or k > 0:
            if i >= 0:
                k += num[i]
                i -= 1
            res.append(k % 10)  # Current digit
            k //= 10             # Carry for the next place value
            
        return res[::-1]  # Reverse to restore correct order
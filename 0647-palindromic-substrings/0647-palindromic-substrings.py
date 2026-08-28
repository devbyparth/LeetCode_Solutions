class Solution:
    def countSubstrings(self, s: str) -> int:
        total_palindromes = 0
        n = len(s)
        
        def expand_around_center(left: int, right: int) -> int:
            count = 0
            # Expand outward as long as characters match and indices stay valid
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        for i in range(n):
            # Odd-length palindromes (single character center)
            total_palindromes += expand_around_center(i, i)
            # Even-length palindromes (center between i and i+1)
            total_palindromes += expand_around_center(i, i + 1)
            
        return total_palindromes
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        # Check if the string is already a palindrome
        return 1 if s == s[::-1] else 2
class Solution(object):
    def repeatedSubstringPattern(self, s):
        # Trick: Concatenate s with itself and check if s exists 
        # inside the joined string (excluding first and last characters)
        return s in (s + s)[1:-1]
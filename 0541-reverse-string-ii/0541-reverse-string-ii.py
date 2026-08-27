class Solution(object):
    def reverseStr(self, s, k):
        # Convert string to list since Python strings are immutable
        chars = list(s)
        
        # Step through string in chunks of 2k
        for i in range(0, len(chars), 2 * k):
            # Reverse the first k characters of the 2k block
            chars[i : i + k] = reversed(chars[i : i + k])
            
        return "".join(chars)
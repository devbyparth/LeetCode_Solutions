class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Step 1: skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: check sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # Step 3: read digits
        result = 0
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        # Step 4: apply sign
        result *= sign

        # Step 5: clamp to 32-bit signed integer range
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN

        return result
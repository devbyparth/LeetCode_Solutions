class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        size = len(digits)
        
        # Step 1: Find the first decreasing digit from the right (pivot)
        i = size - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
            
        # If no such element exists, digits are in descending order
        if i == -1:
            return -1
            
        # Step 2: Find the smallest digit to the right of 'i' that is greater than digits[i]
        j = size - 1
        while digits[j] <= digits[i]:
            j -= 1
            
        # Step 3: Swap pivot and the identified digit
        digits[i], digits[j] = digits[j], digits[i]
        
        # Step 4: Reverse the sequence from i + 1 to the end
        digits[i + 1:] = reversed(digits[i + 1:])
        
        # Step 5: Convert back to integer and check 32-bit signed integer overflow
        ans = int("".join(digits))
        
        MAX_INT = 2**31 - 1
        return ans if ans <= MAX_INT else -1
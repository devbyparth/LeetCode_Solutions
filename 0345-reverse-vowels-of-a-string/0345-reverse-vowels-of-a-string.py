class Solution(object):
    def reverseVowels(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        chars = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while chars[left] not in vowels and left < right:
                left += 1
            while chars[right] not in vowels and left < right:
                right -= 1

            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        
        return ''.join(chars)
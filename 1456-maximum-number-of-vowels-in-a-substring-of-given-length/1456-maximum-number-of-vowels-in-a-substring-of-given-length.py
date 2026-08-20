class Solution(object):
    def maxVowels(self, s, k):
        vowels = set('aeiou')

        cur_vowel = sum([1 for i in range(k) if s[i] in vowels])
        max_vowel = cur_vowel
        for i in range(k, len(s)):
            if max_vowel == k:
                return k
            
            if s[i] in vowels:
                cur_vowel += 1
            if s[i-k] in vowels:
                cur_vowel -= 1
            max_vowel = max(max_vowel, cur_vowel)
        
        return max_vowel
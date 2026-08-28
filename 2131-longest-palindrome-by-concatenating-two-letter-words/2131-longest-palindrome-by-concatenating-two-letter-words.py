from collections import Counter
class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        count = Counter(words)
        length = 0
        central_found = False

        for word, freq in count.items():
            # Case 1: Palindromic words like "gg", "xx"
            if word[0] == word[1]:
                # Pairs of identical symmetric words contribute 4 to length
                length += (freq // 2) * 4
                # If there's an odd count, one can go in the center
                if freq % 2 == 1:
                    central_found = True
            # Case 2: Non-palindromic words like "ab"
            else:
                reversed_word = word[::-1]
                # To avoid double-counting pairs (e.g., processing both "ab" and "ba")
                if word < reversed_word:
                    pairs = min(freq, count[reversed_word])
                    length += pairs * 4

        # Add 2 if we can place one symmetric word in the absolute center
        if central_found:
            length += 2

        return length
class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for ch, w in zip(pattern, words):
            if ch in char_to_word and char_to_word[ch] != w:
                return False
            if w in word_to_char and word_to_char[w] != ch:
                return False
            char_to_word[ch] = w
            word_to_char[w] = ch
        
        return True
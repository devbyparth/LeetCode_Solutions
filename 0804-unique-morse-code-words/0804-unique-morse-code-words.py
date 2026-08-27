class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        
        # Transform each word to Morse code and store in a set for unique counts
        unique_transformations = {
            "".join(morse[ord(char) - ord('a')] for char in word)
            for word in words
        }
        
        return len(unique_transformations)
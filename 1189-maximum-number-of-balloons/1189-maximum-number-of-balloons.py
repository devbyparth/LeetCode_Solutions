from collections import Counter
class Solution(object):
    def maxNumberOfBalloons(self, text):

        countText = Counter(text)
        balloon = Counter("balloon")

        result = float('inf')

        for char in balloon:
            result = min(result, countText[char] // balloon[char])
        
        return result
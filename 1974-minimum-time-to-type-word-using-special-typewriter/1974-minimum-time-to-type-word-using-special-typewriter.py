class Solution(object):
    def minTimeToType(self, word):

        time = 0
        prev = 0

        for char in word:
            curr = ord(char) - ord('a')
            diff = abs(prev - curr)

            diff = min(diff, 26-diff)
            time += diff + 1
            prev = curr
        return time
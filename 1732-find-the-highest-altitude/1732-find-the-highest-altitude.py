class Solution(object):
    def largestAltitude(self, gain):
        highestAltitude = 0
        currentAltitude = 0

        for i in range(len(gain)):
            currentAltitude = currentAltitude + gain[i]
            highestAltitude = max(currentAltitude, highestAltitude)

        return highestAltitude
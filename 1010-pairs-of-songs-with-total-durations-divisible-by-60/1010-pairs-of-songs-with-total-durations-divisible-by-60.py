class Solution(object):
    def numPairsDivisibleBy60(self, time):
        count = 0
        hMap = {}

        for dur in time:

            remainder = dur % 60

            complement = (60-remainder) % 60

            if complement in hMap:
                count += hMap[complement]
            
            hMap[remainder] = hMap.get(remainder, 0) + 1
        
        return count
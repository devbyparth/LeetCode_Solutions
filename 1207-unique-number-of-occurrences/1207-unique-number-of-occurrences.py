from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        countMap = Counter(arr)
        check_set = set(countMap.values())
        
        if len(check_set) == len(countMap):
            return True
        else:
            return False
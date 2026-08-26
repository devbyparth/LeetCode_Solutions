class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        res = []
        for s in spells:
            # Binary Search here

            low, high = 0, len(potions)-1
            idx = len(potions)
            while low <= high:
                mid = (low + high) // 2

                if s * potions[mid] >= success:
                    high = mid - 1
                    idx = mid
                else:
                    low = mid + 1
            res.append(len(potions) - idx)
        return res
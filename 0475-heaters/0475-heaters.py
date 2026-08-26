class Solution(object):
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()

        def canCover(radius):
            i = 0  # pointer for houses
            for h in heaters:
                left_bound = h - radius
                right_bound = h + radius
                # Move house pointer as long as houses are within current heater's range
                while i < len(houses) and left_bound <= houses[i] <= right_bound:
                    i += 1
                if i == len(houses):
                    return True
            return i == len(houses)

        # Binary Search on Radius Range: [0, max_possible_distance]
        low = 0
        high = max(abs(houses[-1] - heaters[0]), abs(heaters[-1] - houses[0]))
        ans = high

        while low <= high:
            mid = (low + high) // 2

            if canCover(mid):
                ans = mid
                high = mid - 1  # Try finding a smaller valid radius
            else:
                low = mid + 1   # Radius too small, increase it

        return ans
class Solution(object):
    def minEatingSpeed(self, piles, h):
        low, high = 1, max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            # Calculate total hours needed at speed 'mid'
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours <= h:
                ans = mid         # 'mid' works, try to find a smaller valid speed
                high = mid - 1
            else:
                low = mid + 1     # 'mid' is too slow, increase speed
        return ans
class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m*k > len(bloomDay):
            return -1

        low, high = min(bloomDay), max(bloomDay)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            bouquets = 0
            flowers = 0

            for day in bloomDay:
                if day <= mid:
                    flowers += 1

                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            if bouquets >= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
class Solution(object):
    def shipWithinDays(self, weights, days):
        def countDays(d):
            days, temp = 1, d
            for w in weights:
                if temp - w >= 0:
                    temp = temp - w
                else:
                    days += 1
                    temp = d - w
            return days
        
        low, high = max(weights), sum(weights)
        ans = 0
        while low <= high:
            mid = (low + high) // 2

            cur_day = countDays(mid)

            if cur_day > days:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        return ans
class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        
        low, high = 0, x//2
        ans = 0
        while low <= high:
            mid = (low + high) //2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
class Solution(object):
    def isPerfectSquare(self, num):
        if num == 1:
            return True
        
        low, high = 2, num//2

        while low <= high:
            mid = (low + high) // 2
            
            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        high = max(candies)

        result = []
        for nums in candies:
            if nums+extraCandies >= high:
                result.append(True)
            else:
                result.append(False)
        
        return result
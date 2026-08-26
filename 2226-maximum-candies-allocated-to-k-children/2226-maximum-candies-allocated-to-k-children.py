class Solution:
    def maximumCandies(self, candies, k):
        # If total candies are less than k children, each gets 0
        if sum(candies) < k:
            return 0

        # Binary search range for max candies per child
        low, high = 1, max(candies)
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            # Total children that can get at least `mid` candies
            children_fed = sum(c // mid for c in candies)

            if children_fed >= k:
                ans = mid
                low = mid + 1   # Try for a larger pile size
            else:
                high = mid - 1  # `mid` is too large, reduce pile size

        return ans
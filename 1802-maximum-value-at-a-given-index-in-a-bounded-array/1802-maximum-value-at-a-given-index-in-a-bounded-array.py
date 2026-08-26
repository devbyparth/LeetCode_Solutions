class Solution:
    def maxValue(self, n, index, maxSum):
        def get_side_sum(count, peak):
            # Helper to calculate sum for `count` elements starting from peak - 1 downwards
            if count == 0:
                return 0

            if peak - 1 >= count:
                # Arithmetic progression: from (peak - 1) down to (peak - count)
                last = peak - count
                return count * (peak - 1 + last) // 2
            else:
                # Progression decreases to 1, rest are padded with 1s
                ones = count - (peak - 1)
                return (peak * (peak - 1)) // 2 + ones

        left, right = 1, maxSum
        ans = 1

        while left <= right:
            mid = (left + right) // 2

            left_sum = get_side_sum(index, mid)
            right_sum = get_side_sum(n - 1 - index, mid)
            total = left_sum + mid + right_sum

            if total <= maxSum:
                ans = mid
                left = mid + 1  # Try for a larger peak value
            else:
                right = mid - 1  # Peak value too large

        return ans
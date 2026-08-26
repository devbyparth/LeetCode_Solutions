import random
import bisect

class Solution:

    def __init__(self, w):
        # Prefix sums array to store cumulative weight thresholds
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self):
        # Generate a random integer in range [1, total_sum]
        target = random.randint(1, self.total_sum)
        # Binary search for the first index with prefix_sum >= target
        return bisect.bisect_left(self.prefix_sums, target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
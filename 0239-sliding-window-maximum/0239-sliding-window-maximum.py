from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # Stores indices of elements
        res = []

        for i, num in enumerate(nums):
            # 1. Remove indices that fall outside the current window
            if q and q[0] <= i - k:
                q.popleft()

            # 2. Maintain monotonically decreasing order in deque
            while q and nums[q[-1]] <= num:
                q.pop()

            q.append(i)

            # 3. Append the max element (at the front of deque) once window reaches size k
            if i >= k - 1:
                res.append(nums[q[0]])

        return res
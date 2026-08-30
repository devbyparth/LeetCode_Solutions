from collections import deque
from itertools import accumulate
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix = list(accumulate(nums, initial=0))
        dq = deque()
        min_len = float('inf')
        
        for i, p in enumerate(prefix):
            while dq and p - prefix[dq[0]] >= k:
                min_len = min(min_len, i - dq.popleft())
            while dq and prefix[dq[-1]] >= p:
                dq.pop()
            dq.append(i)
        
        return min_len if min_len != float('inf') else -1
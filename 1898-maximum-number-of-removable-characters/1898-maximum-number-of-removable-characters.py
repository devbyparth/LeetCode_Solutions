class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def canFormSubsequence(k: int) -> bool:
            # Mark the first k elements of removable as disabled
            removed = [False] * len(s)
            for i in range(k):
                removed[removable[i]] = True

            # Check if p is still a subsequence of s
            i1 = i2 = 0
            len_s, len_p = len(s), len(p)

            while i1 < len_s and i2 < len_p:
                if not removed[i1] and s[i1] == p[i2]:
                    i2 += 1
                i1 += 1

            return i2 == len_p

        # Binary Search on k (number of elements to remove: 0 to len(removable))
        left, right = 0, len(removable)
        res = 0

        while left <= right:
            mid = (left + right) // 2
            if canFormSubsequence(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res
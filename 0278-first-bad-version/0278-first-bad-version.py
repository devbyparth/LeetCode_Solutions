# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        low, high = 1, n
        first_bad = 0

        while low <= high:
            mid = (low + high) // 2

            if isBadVersion(mid):
                first_bad = mid
                high = mid - 1
            else:
                low = mid + 1
        return first_bad
class Solution(object):
    def hIndex(self, citations):
        if len(citations) == 0:
            return 0
        left, right = 0, len(citations)-1

        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= len(citations) - mid:
                right = mid - 1
            else:
                left = mid + 1
        return len(citations) - left
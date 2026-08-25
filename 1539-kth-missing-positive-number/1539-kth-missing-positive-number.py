class Solution(object):
    def findKthPositive(self, arr, k):
        low, high = 0, len(arr)-1
        pre_missing = 0
        while low <= high:
            mid = (low + high) // 2

            missing = arr[mid] - (mid + 1)

            if missing < k:
                low = mid + 1
            else:
                high = mid - 1
        return k + high + 1
        # return k + low
        # This is also valid becoz if we notice carefully in end low = high + 1
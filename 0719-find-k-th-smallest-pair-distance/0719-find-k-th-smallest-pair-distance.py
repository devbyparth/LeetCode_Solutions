class Solution(object):
    def smallestDistancePair(self, nums, k):
        def window(nums, d):
            i, j, n = 0, 1, len(nums)
            pairCount = 0
            while j < n:
                while nums[j] - nums[i] > d:
                    i = i + 1
                pairCount += j-i
                j = j + 1
            return pairCount

        nums.sort()
        low, high = 0, nums[-1]-nums[0]

        result = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            countPair = window(nums, mid)

            if countPair < k:
                low = mid + 1
            else:
                result = mid    # Storing mid as a possible result
                high = mid - 1
        return result
class Solution(object):
    def findMin(self, nums):
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                # Minimum must be strictly in the right unsorted portion
                low = mid + 1
            elif nums[mid] < nums[high]:
                # Right portion is sorted; minimum is at mid or to its left
                high = mid
            else:
                # Duplicates detected; safely shrink high boundary by 1
                high -= 1

        return nums[low]
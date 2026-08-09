class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        minimum = float('inf')
        while left <= right:
            mid = (left + right) // 2

            # Right Part Sorted
            if nums[mid] <= nums[right]:
                minimum = min(minimum, nums[mid])
                right = mid - 1

            # Left Part Sorted
            else:
                minimum = min(minimum, nums[left])
                left = mid + 1

        return minimum
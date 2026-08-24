class Solution(object):
    def singleNonDuplicate(self, nums):
        if len(nums) == 1: return nums[0]
        if nums[0] != nums[1]: return nums[0]
        if nums[-1] != nums[-2]: return nums[-1]

        low, high = 1, len(nums)-2

        while low <= high:
            mid = (low + high) // 2

            if nums[mid-1] != nums[mid] != nums[mid+1]:
                return nums[mid]

            if mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    low = mid + 1
                elif nums[mid] == nums[mid-1]:
                    high = mid - 1
                else:
                    return nums[mid]
            else:
                if nums[mid] == nums[mid-1]:
                    low = mid + 1
                elif nums[mid] == nums[mid+1]:
                    high = mid - 1
                else:
                    return nums[mid]
        return -1
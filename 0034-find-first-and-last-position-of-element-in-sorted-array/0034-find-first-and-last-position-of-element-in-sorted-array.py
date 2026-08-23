class Solution(object):
    def searchRange(self, nums, target):
        def binary_search(find_first):
            low, high = 0, len(nums) - 1
            bound = -1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    bound = mid
                    if find_first:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return bound
        lb = binary_search(True)
        if lb == -1:
            return [-1, -1]
        ub = binary_search(False)
        return [lb, ub]
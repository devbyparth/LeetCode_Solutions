class Solution(object):
    def maxAscendingSum(self, nums):
        sub_array = [nums[0]]
        max_sum = sum(sub_array)
        for i in range(len(nums)):
            if i == 0:
                continue
            if nums[i-1] < nums[i]:
                sub_array.append(nums[i])
                max_sum = max(max_sum, sum(sub_array))
            else:
                sub_array = [nums[i]]
                max_sum = max(max_sum, sum(sub_array))
        
        return max_sum
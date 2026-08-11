class Solution(object):
    def checkSubarraySum(self, nums, k):
        remainder_index = {0:-1}
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k if k!=0 else prefix_sum

            if remainder in remainder_index:
                if i - remainder_index[remainder] >= 2:
                    return True
            else:
                remainder_index[remainder] = i

        return False
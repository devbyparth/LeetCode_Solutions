class Solution(object):
    def shuffle(self, nums, n):
        res = []
        i = 0
        while n < len(nums):
            res.append(nums[i])
            i += 1
            res.append(nums[n])
            n += 1
        return res
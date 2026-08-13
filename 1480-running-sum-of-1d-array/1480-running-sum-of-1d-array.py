class Solution(object):
    def runningSum(self, nums):
        sumRun = nums[0]
        result = [sumRun]

        for i in range(1, len(nums)):
            sumRun += nums[i]
            result.append(sumRun)
        
        return result
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        high = max(nums)

        temp = [0]  * (high+1)

        for i in nums:
            temp[i] += 1

        preSum = []

        count = 0
        for i in range(len(temp)):
            count += temp[i]
            preSum.append(count)

        result = []
        for num in nums:
            result.append(preSum[num-1] if num > 0 else 0)

        return result
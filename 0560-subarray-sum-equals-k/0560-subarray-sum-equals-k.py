class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        cur_sum = 0
        freqMap = {0:1}

        for num in nums:
            cur_sum += num
            count += freqMap.get(cur_sum - k, 0)
            freqMap[cur_sum] = freqMap.get(cur_sum, 0) + 1

        return count
class Solution(object):
    def subarraysDivByK(self, nums, k):
        countMAP = {0: 1}
        result = 0
        cur_sum = 0

        for i in nums:
            cur_sum += i
            remainder = cur_sum % k

            if remainder in countMAP:
                result += countMAP[remainder]
            countMAP[remainder] = countMAP.get(remainder, 0) + 1
        
        return result
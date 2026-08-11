class Solution(object):
    def findErrorNums(self, nums):
        result = []
        check_set = set()
        n = len(nums)
        cur_sum = 0
        for num in nums:
            cur_sum += num
            if num in check_set:
                result.append(num)
            else:
                check_set.add(num)
        missing = ((n * (n+1)) // 2) - (cur_sum - result[0])
        result.append(missing)
        return result
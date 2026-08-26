import bisect
class Solution(object):
    def answerQueries(self, nums, queries):
        nums.sort()
        
        # Build prefix sums in-place
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            
        res = []
        for q in queries:
            i = bisect.bisect_right(nums, q)
            res.append(i)
        return res
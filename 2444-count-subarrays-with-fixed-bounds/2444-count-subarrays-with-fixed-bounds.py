class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        bad_idx, min_idx, max_idx = -1, -1, -1

        ans = 0
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                bad_idx = i
            
            if num == minK:
                min_idx = i
            if num == maxK:
                max_idx = i
            
            valid_start = min(min_idx,max_idx) - bad_idx

            if valid_start > 0:
                ans += valid_start
        return ans
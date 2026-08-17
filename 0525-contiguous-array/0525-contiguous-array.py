class Solution(object):
    def findMaxLength(self, nums):
        seen = {0: -1}
        count = 0
        max_len = 0

        for i, num in enumerate(nums):
            count += 1 if num==1 else -1

            if count in seen:
                max_len = max(max_len, i - seen[count])
            else:
                seen[count] = i
        
        return max_len
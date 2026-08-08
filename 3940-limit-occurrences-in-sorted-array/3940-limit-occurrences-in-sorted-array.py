class Solution(object):
    def limitOccurrences(self, nums, k):
        reset = k
        ans = [nums[0], ]
        k = k-1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                if k > 0:
                    ans.append(nums[i-1])
                    k -= 1
                else:
                    continue
            else:
                k = reset - 1
                ans.append(nums[i])

        return ans
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        result_list = []

        for i in range(len(nums)):

            if i != 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                m, n = j+1, len(nums)-1

                while m < n:
                    total = nums[i] + nums[j] + nums[m] + nums[n]
                    if total < target:
                        m = m+1
                        while nums[m] == nums[m-1] and m < n:
                            m += 1

                    elif total > target:
                        n = n-1
                        while nums[n] == nums[n+1] and m < n:
                            n -= 1

                    else:
                        result_list.append([nums[i], nums[j], nums[m], nums[n]])
                        m = m+1
                        while nums[m] == nums[m-1] and m < n:
                            m += 1
                        n = n-1
                        while nums[n] == nums[n+1] and m < n:
                            n -= 1

        return result_list
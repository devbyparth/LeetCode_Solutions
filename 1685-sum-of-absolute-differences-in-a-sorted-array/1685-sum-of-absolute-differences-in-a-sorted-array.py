class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0
        ans = []

        for i in range(n):
            right_sum = total_sum - left_sum - nums[i]

            left_count = i
            right_count = n - i - 1

            left_diff = (nums[i] * left_count) - left_sum
            right_diff = right_sum - (nums[i] * right_count)

            ans.append(left_diff + right_diff)

            left_sum += nums[i]

        return ans
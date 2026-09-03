class Solution:
    def getSubsets(self, nums, path, i):
        if i == len(nums):
            return [path[:]]
        # Branch 1: Include nums[i]
        path.append(nums[i])
        with_num = self.getSubsets(nums, path, i+1)
        path.pop()

        # Skip all duplicate elements for the exclude branch
        while i+1 < len(nums) and nums[i] == nums[i+1]: i += 1

        # Branch 2: Exclude nums[i] (and all duplicate instances of it)
        without_num = self.getSubsets(nums, path, i+1)
        return with_num + without_num

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.getSubsets(nums, [], 0)
class Solution:
    def get_subsets(self, nums, path, i):
        # Base case: reached the end of nums, return a list containing this subset copy
        if i == len(nums):
            return [path[:]]
        
        # Branch 1: Include nums[i]
        path.append(nums[i])
        with_num = self.get_subsets(nums, path, i + 1)
        
        # Backtrack
        path.pop()
        
        # Branch 2: Exclude nums[i]
        without_num = self.get_subsets(nums, path, i + 1)
        
        # Combine subsets from both decisions and return
        return with_num + without_num

    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.get_subsets(nums, [], 0)
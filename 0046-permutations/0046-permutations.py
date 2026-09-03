class Solution:
    def getPer(self, nums, idx, ans):
        if idx == len(nums):
            # Append a snapshot copy of nums
            ans.append(nums[:])
            return
        
        # Loop from `idx` to swap only remaining available choices
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.getPer(nums, idx + 1, ans)
            nums[idx], nums[i] = nums[i], nums[idx]  # Backtrack

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.getPer(nums, 0, ans)
        return ans
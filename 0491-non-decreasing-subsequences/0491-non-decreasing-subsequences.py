class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, seq):
            if len(seq) >= 2:
                res.append(seq[:])
            
            used = set()

            for i in range(start, len(nums)):
                if (seq and nums[i] < seq[-1]) or (nums[i] in used):
                    continue

                used.add(nums[i])
                seq.append(nums[i])
                backtrack(i+1, seq)
                seq.pop()
        
        backtrack(0, [])
        return res
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start_index, remain, seq):
            if remain == 0:
                res.append(seq[:])
                return
            
            for i in range(start_index, len(candidates)):
                if candidates[i] > remain:
                    break
                if i > start_index and candidates[i-1] == candidates[i]: continue
                # Take the element
                seq.append(candidates[i])
                backtrack(i+1, remain - candidates[i], seq)
                # Not take
                seq.pop()

        backtrack(0, target, [])
        return res
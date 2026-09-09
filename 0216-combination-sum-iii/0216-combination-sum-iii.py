class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(start_index, remain, seq):
            if len(seq) == k and remain == 0:
                res.append(seq[:])
                return
            
            if len(seq) > k:
                return
            
            for i in range(start_index, 10):
                if remain > n:
                    break
                seq.append(i)
                backtrack(i+1, remain-i, seq)
                seq.pop()
        backtrack(1, n, [])
        return res
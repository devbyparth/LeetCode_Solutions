class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(idx: int, comb: list):
            if len(comb) == k:
                res.append(comb[:])
                return
            
            for i in range(idx, n+1):
                comb.append(i)
                backtrack(i+1, comb)
                comb.pop()
        
        backtrack(1, [])
        return res
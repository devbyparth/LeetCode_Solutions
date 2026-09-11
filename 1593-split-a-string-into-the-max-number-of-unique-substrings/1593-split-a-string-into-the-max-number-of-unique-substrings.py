class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        seen = set()
        best = 0
        
        def backtrack(start: int):
            nonlocal best
            if start == n:
                best = max(best, len(seen))
                return
            
            # prune: even if every remaining char became its own unique piece,
            # can we still beat the current best?
            if len(seen) + (n - start) <= best:
                return
            
            for end in range(start + 1, n + 1):
                segment = s[start:end]
                if segment not in seen:
                    seen.add(segment)
                    backtrack(end)
                    seen.remove(segment)      # undo
        
        backtrack(0)
        return best
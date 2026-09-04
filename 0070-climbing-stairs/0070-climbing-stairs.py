class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def backtrack(i):
            if i == n: return 1
            if i > n: return 0
            
            # 1. Check if we already calculated ways to reach 'n' from step 'i'
            if i in memo:
                return memo[i]

            # 2. Store the result in memo before returning
            memo[i] = backtrack(i + 1) + backtrack(i + 2)
            return memo[i]

            return memo[i]
        
        count = backtrack(0)
        return count
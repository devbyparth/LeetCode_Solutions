class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD, res, stack = 10**9 + 7, 0, []
        
        for i, n in enumerate(arr + [0]):
            while stack and (i == len(arr) or arr[stack[-1]] > n):
                j = stack.pop()
                left = j - stack[-1] if stack else j + 1
                right = i - j
                res = (res + arr[j] * left * right) % MOD
            stack.append(i)
            
        return res
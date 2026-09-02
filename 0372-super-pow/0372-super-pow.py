class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        MOD = 1337
        
        # Helper: (x^k) % 1337
        def pow_mod(x: int, k: int) -> int:
            x %= MOD
            res = 1
            for _ in range(k):
                res = (res * x) % MOD
            return res

        # Recursive helper operating on index pointer (right to left)
        def solve(idx: int) -> int:
            if idx < 0:
                return 1
            
            last_digit = b[idx]
            # Recursively solve for the prefix of the array
            part1 = solve(idx - 1)
            
            # Combine: (part1^10 * a^last_digit) % 1337
            term1 = pow_mod(part1, 10)
            term2 = pow_mod(a, last_digit)
            
            return (term1 * term2) % MOD

        return solve(len(b) - 1)
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        even_positions = (n + 1) // 2  # Indices 0, 2, 4... (5 choices: 0, 2, 4, 6, 8)
        odd_positions = n // 2         # Indices 1, 3, 5... (4 choices: 2, 3, 5, 7)
        
        # Fast modular exponentiation O(log n)
        even_count = pow(5, even_positions, MOD)
        odd_count = pow(4, odd_positions, MOD)
        
        return (even_count * odd_count) % MOD
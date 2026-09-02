class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Base case: Row 1 always starts with 0
        if n == 1:
            return 0
        
        # Find parent value in the previous row
        parent = self.kthGrammar(n - 1, (k + 1) // 2)
        
        # Odd k -> left child (matches parent)
        # Even k -> right child (flipped parent)
        return parent if k % 2 == 1 else 1 - parent
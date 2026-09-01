class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for n in nums:
            xor_all ^= n
        
        mask = xor_all & -xor_all        # rightmost set bit

        a = b = 0
        for n in nums:
            if n & mask:
                a ^= n
            else:
                b ^= n

        return [a, b]
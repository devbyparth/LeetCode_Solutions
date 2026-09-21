class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = [0] * k          # final answer counts
        cur = [0] * k          # cur[x] = # subarrays ending at previous element with remainder x
        for v in nums:
            r = v % k
            nxt = [0] * k
            for x in range(k):
                nxt[x * r % k] += cur[x]   # extend every previous subarray by v
            nxt[r] += 1                    # the subarray that is just [v]
            cur = nxt
            for x in range(k):
                res[x] += cur[x]           # all subarrays ending here are answers
        return res
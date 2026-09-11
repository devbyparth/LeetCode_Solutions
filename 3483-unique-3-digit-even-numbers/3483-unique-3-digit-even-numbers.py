class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        cnt = [0] * 10
        for d in digits:
            cnt[d] = min(cnt[d] + 1, 3)   # cap at 3, that's all we can use

        count = 0
        for h in range(1, 10):                       # hundreds, no leading zero
            if cnt[h] == 0: 
                continue
            for t in range(10):                       # tens
                used_t = 1 if t == h else 0
                if cnt[t] <= used_t:
                    continue
                for u in range(0, 10, 2):              # units, must be even
                    used_u = (1 if u == h else 0) + (1 if u == t else 0)
                    if cnt[u] <= used_u:
                        continue
                    count += 1
        return count
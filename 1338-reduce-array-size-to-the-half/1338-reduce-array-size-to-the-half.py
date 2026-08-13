from collections import Counter
class Solution(object):
    def minSetSize(self, arr):
        countInt = Counter(arr)
        n = len(arr)
        target = n // 2 if n % 2 == 0 else n//2 + 1

        cur = 0
        setInt = set()
        for k, v in countInt.most_common():
            setInt.add(k)
            cur += v
            if cur >= target:
                return len(setInt)
        
        return len(setInt)
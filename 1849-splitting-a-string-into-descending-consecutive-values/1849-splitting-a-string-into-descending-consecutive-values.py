class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def backtrack(start: int, prev: int) -> bool:
            if start == n:
                return True

            for end in range(start, n):
                segment = s[start:end + 1]
                curr = int(segment)          # Python ints handle big numbers natively

                if curr == prev - 1:
                    if backtrack(end + 1, curr):
                        return True
                elif curr >= prev:
                    # numbers only grow as segment gets longer — no point continuing
                    break

            return False

        # try every possible length for the FIRST number
        for i in range(n - 1):               # must leave at least 1 char for the rest
            first = int(s[:i + 1])
            if backtrack(i + 1, first):
                return True

        return False
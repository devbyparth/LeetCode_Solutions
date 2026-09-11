class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = []

        def backtrack(remaining: int, current: int):
            # Base case: number has n digits, save it
            if remaining == 0:
                result.append(current)
                return

            last_digit = current % 10
            next_digits = {last_digit + k, last_digit - k}

            for d in next_digits:
                if 0 <= d <= 9:
                    backtrack(remaining - 1, current * 10 + d)
        # Start with each possible first digit (1-9, no leading zero)
        for start in range(1, 10):
            backtrack(n - 1, start)

        return result
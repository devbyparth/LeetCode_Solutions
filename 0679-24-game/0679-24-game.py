class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6

        def solve(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPS

            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    # build the remaining list (all nums except i and j)
                    rest = [nums[k] for k in range(n) if k != i and k != j]
                    a, b = nums[i], nums[j]

                    candidates = [a + b, a - b, a * b]
                    if abs(b) > EPS:
                        candidates.append(a / b)

                    for val in candidates:
                        if solve(rest + [val]):
                            return True
            return False

        return solve([float(c) for c in cards])
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans, stack = [], []

        for i in range(len(temperatures)-1, -1, -1):
            while stack and temperatures[i] >= stack[-1][1]:
                stack.pop()
            if not stack:
                ans.append(0)
            else:
                ans.append(stack[-1][0] - i)
            stack.append((i, temperatures[i]))
        return ans[::-1]
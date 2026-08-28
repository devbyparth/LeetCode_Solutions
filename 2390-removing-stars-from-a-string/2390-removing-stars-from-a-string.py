class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack and ch == '*':
                stack.pop()
            elif not stack and ch == '*':
                pass
            else:
                stack.append(ch)
        return ''.join(stack)
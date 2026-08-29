class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {char: i for i, char in enumerate(s)}
        stack = []
        seen = set()

        for i, char in enumerate(s):
            if char in seen:
                continue

            # Pop larger characters if they appear again later in the string
            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

        return "".join(stack)
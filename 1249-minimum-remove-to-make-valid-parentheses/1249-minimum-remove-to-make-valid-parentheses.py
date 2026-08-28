class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_list = list(s)
        stack = []  # Stores indices of unmatched '('

        for i, char in enumerate(s_list):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()  # Matched with a previous '('
                else:
                    s_list[i] = ''  # Unmatched ')', mark for removal

        # Remove remaining unmatched '('
        while stack:
            s_list[stack.pop()] = ''

        return "".join(s_list)
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ''
        curr_num = 0

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                # Push state to stack and reset tracking variables
                stack.append((curr_str, curr_num))
                curr_str = ''
                curr_num = 0
            elif char == ']':
                # Pop state and construct decoded string segment
                prev_str, num = stack.pop()
                curr_str = prev_str + curr_str * num
            else:
                curr_str += char
        return curr_str
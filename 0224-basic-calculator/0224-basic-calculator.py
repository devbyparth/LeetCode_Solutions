class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        cur_num = 0
        sign = 1

        for ch in s:
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            elif ch in {'+', '-'}:
                res += sign * cur_num
                cur_num = 0
                sign = 1 if ch == '+' else -1
            elif ch == '(':
                stack.append(res)
                stack.append(sign)

                res = 0
                sign = 1
            elif ch == ')':
                res += sign * cur_num
                cur_num = 0
                res *= stack.pop()
                res += stack.pop()

        return res + (sign * cur_num)
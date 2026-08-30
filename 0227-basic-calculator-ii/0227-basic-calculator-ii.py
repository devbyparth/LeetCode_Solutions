class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        last_operator = '+'
        s += '+'  # Dummy operator to ensure the final number is processed

        for char in s:
            if char.isdigit():
                current_number = (current_number * 10) + int(char)
            elif char in "+-*/":
                if last_operator == '+':
                    stack.append(current_number)
                elif last_operator == '-':
                    stack.append(-current_number)
                elif last_operator == '*':
                    stack.append(stack.pop() * current_number)
                elif last_operator == '/':
                    # In Python, integer division towards zero requires int(a/b)
                    stack.append(int(stack.pop() / current_number))
                
                # Reset for the next number
                last_operator = char
                current_number = 0

        return sum(stack)
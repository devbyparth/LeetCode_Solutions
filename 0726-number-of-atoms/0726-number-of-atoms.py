from collections import Counter

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [Counter()]
        i, n = 0, len(formula)
        
        while i < n:
            if formula[i] == '(':
                stack.append(Counter())
                i += 1
            elif formula[i] == ')':
                i += 1
                # Parse multiplier following ')'
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[i_start:i] or 1)
                
                # Pop scope map, multiply counts, and merge into parent scope
                top_scope = stack.pop()
                for elem, count in top_scope.items():
                    stack[-1][elem] += count * multiplier
            else:
                # 1. Parse Element Name (1 Uppercase + lowercase letters)
                i_start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                elem = formula[i_start:i]
                
                # 2. Parse Element Quantity
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[i_start:i] or 1)
                
                # Add to active scope
                stack[-1][elem] += count
                
        # Format result alphabetically
        final_counts = stack[0]
        result = []
        for elem in sorted(final_counts.keys()):
            result.append(elem)
            if final_counts[elem] > 1:
                result.append(str(final_counts[elem]))
                
        return "".join(result)
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def add_strings(a: str, b: str) -> str:
            """Add two non-negative integer strings, return result as string."""
            i, j = len(a) - 1, len(b) - 1
            carry, result = 0, []
            while i >= 0 or j >= 0 or carry:
                x = int(a[i]) if i >= 0 else 0
                y = int(b[j]) if j >= 0 else 0
                total = x + y + carry
                result.append(str(total % 10))
                carry = total // 10
                i -= 1
                j -= 1
            return ''.join(reversed(result))

        def check(first: str, second: str, rest: str) -> bool:
            if len(first) > 1 and first[0] == '0':
                return False
            if len(second) > 1 and second[0] == '0':
                return False
            while rest:
                third = add_strings(first, second)
                if not rest.startswith(third):
                    return False
                rest = rest[len(third):]
                first, second = second, third
            return True

        # Try every way to split off the first two numbers.
        for i in range(1, n):
            if i > 1 and num[0] == '0':
                break
            for j in range(i + 1, n):
                first, second, rest = num[:i], num[i:j], num[j:]
                if len(second) > 1 and second[0] == '0':
                    continue
                if check(first, second, rest):
                    return True
        return False
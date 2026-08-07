class Solution(object):
    def addBinary(self, a, b):
        n = len(a) - 1
        m = len(b) - 1
        length = max(len(a), len(b))
        result = []
        carry = 0

        for i in range(length - 1, -1, -1):

            x = a[n] if n >= 0 else '0'
            y = b[m] if m >= 0 else '0'

            if carry:
                if x == '1' and y == '1':
                    result.insert(0, '1')
                    carry = 1
                elif (x == '1' and y == '0') or (x == '0' and y == '1'):
                    result.insert(0, '0')
                    carry = 1
                else:
                    result.insert(0, '1')
                    carry = 0
            else:
                if x == '1' and y == '1':
                    result.insert(0, '0')
                    carry = 1
                elif (x == '1' and y == '0') or (x == '0' and y == '1'):
                    result.insert(0, '1')
                else:
                    result.insert(0, '0')

            n -= 1
            m -= 1

        if carry:
            result.insert(0, '1')

        return ''.join(result)
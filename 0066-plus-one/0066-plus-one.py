class Solution(object):
    def plusOne(self, digits):
            length = len(digits)

            if digits[-1] <= 8:
                digits[-1] = digits[-1] + 1
                return digits

            for i in range(length-1, -1, -1):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] = digits[i] + 1
                    return digits

            digits.insert(0, 1)
            return digits
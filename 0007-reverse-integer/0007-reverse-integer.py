class Solution(object):
    def reverse(self, x):

        if x < 0:
            num = -1 * x
        else:
            num = x

        rev = 0
        while num > 0:
            rev = rev * 10 + num % 10
            num = int(num / 10)

        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        if rev > INT_MAX or rev < INT_MIN:
            return 0

        if x < 0:
            return rev * -1
        else:
            return rev
class Solution(object):
    def titleToNumber(self, columnTitle):
        col_num = 0

        for i, char in enumerate(columnTitle[::-1]):
            val = ord(char) - ord('A') + 1
            col_num += (26 ** i) * val
        return col_num
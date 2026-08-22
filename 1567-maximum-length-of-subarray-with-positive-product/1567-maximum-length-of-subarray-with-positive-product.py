class Solution(object):
    def getMaxLen(self, nums):
        max_len = 0

        left = 0
        first_neg = -1
        neg_count = 0

        for right, num in enumerate(nums):
            if num == 0:
                left = right + 1
                first_neg = -1
                neg_count = 0
            else:
                if num < 0:
                    neg_count += 1
                    if first_neg == -1:
                        first_neg = right

                if neg_count % 2 == 0:
                    max_len = max(max_len, right - left + 1)
                else:
                    max_len = max(max_len, right - first_neg + 1 - 1)
        return max_len
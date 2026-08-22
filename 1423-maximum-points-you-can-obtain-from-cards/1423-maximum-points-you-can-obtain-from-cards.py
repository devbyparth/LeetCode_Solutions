class Solution(object):
    def maxScore(self, cardPoints, k):
        left_sum = sum(cardPoints[:k])
        right_sum = 0

        max_sum = left_sum
        right = len(cardPoints) - 1

        for i in range(k - 1, -1, -1):
            right_sum += cardPoints[right]
            right -= 1
            left_sum -= cardPoints[i]

            cur_sum = left_sum + right_sum
            max_sum = max(max_sum, cur_sum)

        return max_sum
class Solution(object):
    def maximumWealth(self, accounts):

        rows = len(accounts)
        highest = 0
        for row in range(rows):
            cur_sum = sum(accounts[row])
            highest = max(highest, cur_sum)

        return highest
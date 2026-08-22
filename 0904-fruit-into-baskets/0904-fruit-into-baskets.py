class Solution(object):
    def totalFruit(self, fruits):
        windowMap = {}
        left, right, max_len = 0, 0, 0

        while right < len(fruits):
            incoming = fruits[right]
            windowMap[incoming] = windowMap.get(incoming, 0) + 1

            while len(windowMap) > 2:
                outgoing = fruits[left]
                windowMap[outgoing] -= 1
                if windowMap[outgoing] == 0:
                    del windowMap[outgoing]
                left += 1

            cur_len = right - left + 1
            right += 1
            max_len = max(max_len, cur_len)
        return max_len
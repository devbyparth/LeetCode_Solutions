class Solution(object):
    def removeDuplicates(self, s):

        temp = list([s[0],])

        for i in range(1, len(s)):
            if not temp:
                temp.append(s[i])
            elif s[i] == temp[-1]:
                temp.pop(-1)
            else:
                temp.append(s[i])

        return ''.join(temp)

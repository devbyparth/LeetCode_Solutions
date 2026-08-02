class Solution(object):
    def rotateString(self, s, goal):

        if len(s) != len(goal):
            return False

        s = str(s) + str(s)

        if goal in s:
            return True
        else:
            return False

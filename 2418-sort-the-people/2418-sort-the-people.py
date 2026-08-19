class Solution(object):
    def sortPeople(self, names, heights):
        personMap = dict(zip(heights, names))

        return [personMap[h] for h in sorted(heights, reverse=True)]
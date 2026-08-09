class Solution(object):
    def findRestaurant(self, list1, list2):

        minSumIndex = float('inf')
        result = []

        hMap = {}
        for i in range(len(list1)):
            if list1[i] not in hMap:
                hMap[list1[i]] = i

        for i in range(len(list2)):
            if list2[i] in hMap:
                total = hMap[list2[i]] + i
                if total < minSumIndex:
                    minSumIndex = total
                    result = [list2[i]]
                elif total == minSumIndex:
                    result.append(list2[i])
                    
        return result
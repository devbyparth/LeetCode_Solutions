class Solution(object):
    def relativeSortArray(self, arr1, arr2):

        arr2_set = set(arr2)
        arr1_count = {}
        end = []
        for num in arr1:
            if num not in arr2_set:
                end.append(num)
            arr1_count[num] = arr1_count.get(num, 0) + 1
        end.sort()

        result = []

        for num in arr2:
            for _ in range(arr1_count[num]):
                result.append(num)

        return result + end
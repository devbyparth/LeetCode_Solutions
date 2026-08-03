class Solution(object):
    def findLucky(self, arr):

        frequency_map = dict()
        lucky_num = -1

        for num in arr:
            frequency_map[num] = frequency_map.get(num, 0) + 1

        for key, value in frequency_map.items():

            if key == value:
                if lucky_num <= key:
                    lucky_num = key

        return lucky_num
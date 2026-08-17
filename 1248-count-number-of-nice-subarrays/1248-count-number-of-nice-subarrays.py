class Solution(object):
    def numberOfSubarrays(self, nums, k):
        count_map = {0: 1}
        odd_count = 0
        result = 0

        for num in nums:
            if num % 2 == 1:
                odd_count += 1

            if odd_count - k in count_map:
                result += count_map[odd_count - k]

            count_map[odd_count] = count_map.get(odd_count, 0) + 1

        return result
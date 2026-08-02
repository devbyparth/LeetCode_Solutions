class Solution(object):
    def intersect(self, nums1, nums2):

        result = []
        num_counts = {}

        for i in nums1:
            num_counts[i] = num_counts.get(i, 0) + 1

        for i in nums2:
            num_counts[i] = num_counts.get(i, 0) - 1

            if num_counts[i] >= 0:
                result.append(i)

        return result
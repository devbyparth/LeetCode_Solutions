class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2
        left = (n + 1) // 2          # elements in the left half
        low, high = 0, n1

        while low <= high:
            mid1 = (low + high) // 2  # elements taken from nums1
            mid2 = left - mid1        # elements taken from nums2

            l1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
            l2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
            r1 = nums1[mid1] if mid1 < n1 else float('inf')
            r2 = nums2[mid2] if mid2 < n2 else float('inf')

            if l1 <= r2 and l2 <= r1:          # valid partition
                if n % 2 == 1:
                    return float(max(l1, l2))
                return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:                       # took too many from nums1
                high = mid1 - 1
            else:                               # took too few from nums1
                low = mid1 + 1

        return 0.0
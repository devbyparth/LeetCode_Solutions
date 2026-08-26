class Solution(object):
    def findPeakGrid(self, mat):
        def maxElement(mid):
            m, n = len(mat), len(mat[0])
            maxVal = -1
            idx = -1
            for i in range(m):
                if mat[i][mid] > maxVal:
                    maxVal = mat[i][mid]
                    idx = i
            return idx

        low, high = 0, len(mat[0])-1

        while low <= high:
            mid = (low + high) // 2

            row = maxElement(mid)
            left = mat[row][mid-1] if mid-1 >= 0 else -1
            right = mat[row][mid+1] if mid+1 <= len(mat[0])-1 else -1

            if left < mat[row][mid] > right:
                return [row, mid]
            elif mat[row][mid] < left:
                high = mid - 1
            else:
                low = mid + 1
        return [-1, -1]

class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])

        # Virtual 1D array boundaries
        low = 0
        high = (rows * cols) - 1

        while low <= high:
            mid = (low + high) // 2

            # Map 1D index to 2D row and column
            r = mid // cols
            c = mid % cols

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
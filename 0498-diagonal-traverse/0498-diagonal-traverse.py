class Solution(object):
    def findDiagonalOrder(self, mat):
        rows, cols = len(mat), len(mat[0])
        diagonals = rows + cols - 1
        result = []

        for d in range(diagonals):
            if d % 2 == 0:
                i = min(d, rows - 1)
                j = d-i
                while j < cols and i >= 0:
                    result.append(mat[i][j])
                    j += 1
                    i -= 1
            else:
                j = min(d, cols - 1)
                i = d-j
                while j >= 0 and i < rows:
                    result.append(mat[i][j])
                    i += 1
                    j -= 1
        return result
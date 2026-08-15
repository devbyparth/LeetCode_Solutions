class Solution(object):
    def matrixReshape(self, mat, r, c):
        rows = len(mat)
        cols = len(mat[0])
        if r * c != rows * cols:
            return mat
        final = []
        for i in range(rows):
            for j in range(cols):
                final.append(mat[i][j])
        result = []
        idx = 0
        for i in range(r):
            result.append(final[idx:idx+c])
            idx += c
        
        return result
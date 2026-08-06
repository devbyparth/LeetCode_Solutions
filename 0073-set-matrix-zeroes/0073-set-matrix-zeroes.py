class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        row_track = [0 for _ in range(rows)]
        col_track = [0 for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_track[i] = -1
                    col_track[j] = -1

        for i in range(rows):
            for j in range(cols):
                if row_track[i] == -1 or col_track[j] == -1:
                    matrix[i][j] = 0

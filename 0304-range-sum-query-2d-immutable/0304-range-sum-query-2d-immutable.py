class NumMatrix(object):

    def __init__(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefixMatrix = [[0] * (COLS+1) for _ in range(ROWS+1)]
        for rows in range(ROWS):
            prefix = 0
            for cols in range(COLS):
                prefix += matrix[rows][cols]
                above = self.prefixMatrix[rows][cols+1]
                self.prefixMatrix[rows+1][cols+1] = prefix + above

    def sumRegion(self, row1, col1, row2, col2):
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1

        bottomRight = self.prefixMatrix[row2][col2]
        above = self.prefixMatrix[row1-1][col2]
        left = self.prefixMatrix[row2][col1-1]
        topleft = self.prefixMatrix[row1-1][col1-1]

        return bottomRight - above - left + topleft
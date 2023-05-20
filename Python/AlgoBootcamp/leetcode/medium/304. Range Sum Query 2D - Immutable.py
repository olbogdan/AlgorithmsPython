# Given a 2D matrix matrix, handle multiple queries of the following type:
#
# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:
#
# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# You must design an algorithm where sumRegion works on O(1) time complexity.
#
#
#
# Example 1:
#
#
# Input
# ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
# Output
# [null, 8, 11, 12]
#
# Explanation
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# -104 <= matrix[i][j] <= 104
# 0 <= row1 <= row2 < m
# 0 <= col1 <= col2 < n
# At most 104 calls will be made to sumRegion.
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # precalulate prefixes
        # add top/right 0's raw and 0's array
        ROWS, COLS = len(matrix) + 1, len(matrix[0]) + 1
        self.board = [ [0] *  COLS for _ in range(ROWS) ]
        for r in range(1, ROWS):
            for c in range(1, COLS):
                originMatrixVal = matrix[r-1][c-1]
                self.board[r][c] = originMatrixVal + self.board[r - 1][c] + self.board[r][c - 1] - self.board[r-1][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        fullRectangle = self.board[r2][c2]
        leftPrefix = self.board[r2][c1 - 1]
        topPrefix = self.board[r1 - 1][c2]
        topleftItem = self.board[r1 - 1][c1 - 1]
        return fullRectangle - leftPrefix - topPrefix + topleftItem


obj = NumMatrix([[1,1,1],[1,1,1],[1,1,1]])
res = obj.sumRegion(0,0,2,2)
assert res == 9
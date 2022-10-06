# An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).
#
# Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.
# Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
# Output: true
# Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
# Hence, we return true.
# Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
# Output: false
# Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
# Hence, we return false.
from typing import List


def checkValid(matrix: List[List[int]]) -> bool:
    for r in range(len(matrix)):
        rows = set()
        columns = set()
        for c in range(len(matrix)):
            if matrix[r][c] in rows or matrix[c][r] in columns:
                return False
            rows.add(matrix[r][c])
            columns.add(matrix[c][r])
    return True


assert checkValid([[1,1,1],[1,2,3],[1,2,3]]) is False
assert checkValid([[1,2,3],[3,1,2],[2,3,1]]) is True

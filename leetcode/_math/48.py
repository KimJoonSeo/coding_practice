import copy
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        cp = [row[:] for row in matrix]
        for i in range(n):
            for j in range(n):
                matrix[j][n-i-1] = cp[i][j]

Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])
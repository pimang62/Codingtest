'''
[Score After Flipping Matrix]
`m` x `n` binary matrix `grid`
changing all 0's to 1's, and all 1's to 0's

Every row of the matrix, as a binary number
score of the matrix is the "sum"

Return the "highest" possible "score"
after making any number of "moves"

1 <= m, n <= 20

* if 0 in first flip the row
* if num of 0 > 1 flip the col
''' 
from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        answer = (1 << (n - 1)) * m  # 0열은 무조건 다 1

        for j in range(1, n):
            maxi = 1 << (n - 1 - j)
            ones = 0
            for i in range(m):
                if grid[i][j] == grid[i][0]:  # 0열(1)과 같다면
                    ones += 1

            answer += max(ones, m - ones) * maxi

        return answer

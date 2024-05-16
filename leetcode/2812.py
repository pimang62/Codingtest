'''
[Find the Safest Path in a Grid]
`grid` of size `n x n`
a thief if `grid[r][c] = 1`
empty cell if `grid[r][c] = 0`
initially positioned at cell `(0, 0)`

safeness factor of a path 
is defined as the "minimum" manhattan distance

Return the "maximum" safeness factor
'''
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        
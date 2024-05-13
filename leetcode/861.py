'''
[Score After Flipping Matrix]
`m` x `n` binary matrix `grid`
changing all 0's to 1's, and all 1's to 0's

Return the highest possible "score"
after making any number of "moves"
'''
from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        
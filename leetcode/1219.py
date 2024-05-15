'''
[Path with Maximum Gold]
`grid` of size `m` x `n`,
integer representing the amount of "gold"

Return the maximum amount of gold
  - you will collect all the gold in that cell
  - walk one step to the left, right, up, or down
  - can't visit the same cell
  - Never visit a cell with 0
  - start and stop collecting gold from any position

1 <= m, n <= 15
'''
from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        def in_range(a, b):
            return 0 <= a < m and 0 <= b < n

        cnt = 0
        def dfs(i, j, cnt):
            nonlocal answer
            if not in_range(i, j) or grid[i][j] == 0:
                return 0
            
            tmp = grid[i][j]  # 현재 값 기록
            grid[i][j] = 0  # marking
            cnt = tmp + max(dfs(i+1, j, cnt), dfs(i, j+1, cnt), \
                            dfs(i-1, j, cnt), dfs(i, j-1, cnt))  # tmp + (0 or num)
            grid[i][j] = tmp  # Backtracking
            return cnt

        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    answer = max(answer, dfs(i, j, 0))
        
        return answer
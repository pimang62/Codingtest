'''
[Island Perimeter]
given row x col grid
1 land, 0 water
Determine the perimeter of the island.

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

- 주변에 0이거나 not in_range면 +1씩
'''
from typing import List

class Solution:  # My solution
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        
        def in_range(a, b):
            return 0 <= a < N and 0 <= b < M

        answer = 0
        for i in range(N):
            for j in range(M):
                cnt = 0
                if grid[i][j] != 1:
                    continue
                for (dx, dy) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = i+dx, j+dy
                    if not in_range(nx, ny):
                        cnt += 1
                        continue
                    if grid[nx][ny] == 0:
                        cnt += 1
                answer += cnt
        
        return answer

class Solution:  # Iterative
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                    if r > 0 and grid[r-1][c] == 1:
                        perimeter -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        perimeter -= 2
                        
        return perimeter

class Solution:  # DFS
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 1
            if grid[r][c] == -1:
                return 0
            grid[r][c] = -1
            return (dfs(r + 1, c) +
                    dfs(r - 1, c) +
                    dfs(r, c + 1) +
                    dfs(r, c - 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += dfs(r, c)

        return perimeter
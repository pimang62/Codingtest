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
from collections import deque

class Solution:
    def __init__(self):
        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]

    def in_range(self, a, b, n):
        return 0 <= a < n and 0 <= b < n 

    def bfs(self, grid, score):
        n = len(grid)
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j]:  # 1
                    score[i][j] = 0
                    q.append((i, j))

        while q:
            x, y = q.popleft()
            s = score[x][y]

            for k in range(4):
                nx = x + self.dx[k]
                ny = y + self.dy[k]
                if self.in_range(nx, ny, n) and score[nx][ny] > s+1:
                    score[nx][ny] = s+1
                    q.append((nx, ny))

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return 0

        score = [[1e9]*n for _ in range(n)]
        self.bfs(grid, score)

        visited = [[0]*n for _ in range(n)]
        q = [(-score[0][0], 0, 0)]
        heapq.heapify(q)

        while q:
            safe, x, y = heapq.heappop(q)
            safe = -safe

            if x == n-1 and y == n-1:
                return safe

            visited[x][y] = 1

            for k in range(4):
                nx = x + self.dx[k]
                ny = y + self.dy[k]
                if self.in_range(nx, ny, n) and not visited[nx][ny]:
                    s = min(safe, score[nx][ny])
                    heapq.heappush(q, (-s, nx, ny))
                    visited[nx][ny] = 1

        return -1
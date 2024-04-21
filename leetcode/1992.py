'''
[Find All Groups of Farmland]
0-indexed, m by n, 1 a hectare of farmland
These rectangular areas are called "groups"
one group not four-directionally adjacent
Find the "coordinates" of the top left and bottom right corner of each group

[[1,0,0],
 [0,1,1],
 [0,1,1]]

>>> [[0,0,0,0],[1,1,2,2]]
'''
from typing import List
from collections import deque

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        N, M = len(land), len(land[0])
        visited = [[0]*M for _ in range(N)]

        dx = [0, 1, 0, -1]  # 동남서북
        dy = [1, 0, -1, 0]

        def in_range(a, b):
            return 0 <= a < N and 0 <= b < M

        def bfs(x, y):
            q = deque([(x, y)])
            visited[x][y] = 1

            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if not in_range(nx, ny) or visited[nx][ny]:
                        continue
                    if not visited[nx][ny] and land[nx][ny]:  # 1
                        visited[nx][ny] = 1
                        q.append((nx, ny))
            
            return (x, y)

        answer = []
        for i in range(N):
            for j in range(M):
                if not visited[i][j] and land[i][j]:  # 1
                    xx, yy = bfs(i, j)
                    answer.append([i, j, xx, yy])

        return answer
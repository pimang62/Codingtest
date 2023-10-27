import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

from copy import deepcopy
n = int(input())

order = {
    1:[(-2, 0), (-1, 0), (+1, 0), (+2, 0)], 2:[(0, 1), (1, 0), (0, -1), (-1, 0)], 3:[(-1, -1), (-1, +1), (+1, -1), (+1, +1)]
    }

ones = []  # [(1, 2), (2, 1)]
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] == 1:
            ones.append((i, j))
    graph.append(row)


def countbomb(x, y, graph):
    op = graph[x][y]  # operator : 1 2 3
    
    destroyed = set()
    for dx, dy in order[op]:  # [(-2, 0), (-1, 0), (+1, 0), (+2, 0)]
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in destroyed:
            destroyed.add((nx, ny))
    
    return len(destroyed)


res = 0  # 전체 터진 개수 기록

def dfs(cnt, prev):
    global res
    if cnt == len(ones):
        res = max(res, prev)
        return

    for x, y in ones:
        for o in [1, 2, 3]:
            graph[x][y] = o
            prev = countbomb(x, y, graph)
            dfs(cnt+1, prev)
            graph[x][y] = 1

dfs(0, 0)

print(res)
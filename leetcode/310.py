'''
[Minimum Height Trees]
two vertices are connected by exactly one path
without simple cycles is a tree.

0 to n - 1 edges, edges[i] = [ai, bi]
min(h)) are called minimum height trees (MHTs).

nodes left in the queue are "potential" root
of the minimum height trees.
'''
from typing import List
from heapq import heappush, heappop

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # [[1], [0, 2, 3], [1], [1]]
        graph = [[] for _ in range(n)]  # 0-indexed
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # 각 노드에서의 최대 깊이를 저장하기 위한 힙
        min_heap = []
        
        # 각 노드를 시작점으로 하여 DFS 수행
        def dfs(now, parent):
            max_depth = 0
            for nxt in graph[now]:
                if nxt != parent:
                    max_depth = max(max_depth, dfs(nxt, now) + 1)
            return max_depth
        
        for i in range(n):
            depth = dfs(i, -1)  # 부모가 없으므로 -1
            heappush(min_heap, (depth, i))
        
        # 최소 높이를 가진 노드 찾기
        result = []
        min_height = min_heap[0][0]  # 최소 힙이므로 첫 원소의 깊이가 최소 깊이
        
        while min_heap and min_heap[0][0] == min_height:
            result.append(heappop(min_heap)[1])
        
        return result

from collections import deque, defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]  # Only one node, return the root

        # Build graph using adjacency list
        ## {1: [0, 2, 3], 0: [1], 2: [1], 3: [1]}
        graph = defaultdict(list)
        ## [1, 3, 1, 1]
        degrees = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degrees[u] += 1
            degrees[v] += 1

        # Initialize queue with "leaf" nodes (degree == 1)
        q = deque()
        for i in range(n):
            if degrees[i] == 1:
                q.append(i)
        
        remaining_nodes = n
        while remaining_nodes > 2:
            # Remove current leaf nodes
            size = len(q)
            remaining_nodes -= size
            
            for _ in range(size):
                leaf = q.popleft()
                for neighbor in graph[leaf]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        q.append(neighbor)
        
        return list(q)
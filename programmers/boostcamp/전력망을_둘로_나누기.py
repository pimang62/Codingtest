'''
전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록
두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)?

2 <= n <= 100
len(wires) : n-1
'''
from collections import deque
import heapq

def dfs(graph, visited, i):
    #nonlocal graph, visited
    q = deque([i])
    visited[i] = 1
    cnt = 0
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                q.append(nxt)
                cnt += 1
    return cnt  # 몇 덩이?

def solution(n, wires):
    graph = [ [] for _ in range(n+1) ]   # 1-indexed
    for wire in wires:
        a, b = wire
        graph[a].append(b)
        graph[b].append(a)

    result = []   # 어디를 끊었는지 알고 싶다면
    answer = 1e7
    for wire in wires: 
        a, b = wire
        visited = [0] * (n+1)   # 1-indexed

        graph[a].remove(b)
        graph[b].remove(a)

        tmp = abs(dfs(graph, visited, a)-dfs(graph, visited, b))
        answer = min(answer, tmp)
        heapq.heappush(result, (tmp, a, b))

        graph[a].append(b)
        graph[b].append(a)
    
    there = []   # 여기다!
    while result:
        num, a, b = heapq.heappop(result)
        if num == answer:
            there.append((a, b))
    
    return there

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
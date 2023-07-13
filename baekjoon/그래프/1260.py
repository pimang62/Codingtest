'''
[DFS와 BFS]
그래프 양방향!

입력)
n, m, v = map(int, input().split())

graph = [ [] for _ in range(n+1) ]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

'''

n, m, v = map(int, input().split())

graph = [ [] for _ in range(n+1) ]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, visited_dfs, now):
    # 방문 처리
    visited_dfs[now] = True
    for nxt in sorted(graph[now]):     # 정렬시키기!
        # 방문하지 않은 노드만
        if visited_dfs[nxt] == False:
            d.append(nxt)
            dfs(graph, visited_dfs, nxt)
            
    return d


from collections import deque

def bfs(graph, visited_bfs, now):
    q = deque([now])
    visited_bfs[now] = True
    while q:
        now = q.popleft()
        for nxt in sorted(graph[now]):       
            if visited_bfs[nxt] == False:
                q.append(nxt)
                b.append(nxt)
                visited_bfs[nxt] = True
     
    return b


d = [v]  # 첫 노드 기록
b = [v]
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)
now = v    

print(*dfs(graph, visited_dfs, now))
print(*bfs(graph, visited_bfs, now))



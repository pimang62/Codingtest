'''
[숨바꼭질 3]
수빈이의 위치가 x일 때, 
- 걷는다면 1초 후에 x-1 or x+1
- 순간이동 0초 후에 2*x
: 순간이동 후 걷는 것 vs. 그냥 걷는 것

0 <= n, k <= 1e6
n -> x -> k로 가는 가장 빠른 시간?
'''
from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001

def bfs(s):
    q = deque([s])
    visited[s] = 1
    
    while q:
        now = q.popleft()  # 5
        if now == k:
            return visited[now]-1
        
        if 0 <= now*2 <= 100000 and not visited[now*2]:
            visited[now*2] = visited[now]  # 초 업데이트 X
            q.appendleft(now*2)  # 가중치 높은 것 먼저!!
            
        for nxt in (now-1, now+1):
            if 0 <= nxt <= 100000 and not visited[nxt]:
                visited[nxt] += visited[now] + 1
                q.append(nxt)

print(bfs(n))
'''
[스타트링크]
총 F층 -> G층
현재 S층

버튼이 2개
U: 위로, D: 아래로

1 <= s, g <= f <= 1e6
0 <= u, d <= 1e6
1층부터 시작 가장 높은 층 f

버튼을 적어도 몇 번 눌러야 하는지? (최소)
만약, 갈 수 없다면 "use the stairs"
'''
from collections import deque

# 10 1 10 2 1 -> 1 + 2*(u:5) - 1*(d:1)
f, s, g, u, d = map(int, input().split())

res = 1e7 # 최종 최솟값
#         0 1 2 3 .....       10    
stairs = [0 for _ in range(f+1)]  # 0-indexed

def bfs(s):
    q = deque([s])
    stairs[s] += 1  # 1
    
    while q:
        now = q.popleft()
        if now == g:
            return stairs[now]-1  # 초깃값이 1이므로!
        for nxt in [now-d, now+u]:
            if 1 <= nxt <= f and not stairs[nxt]:
                stairs[nxt] += stairs[now] + 1  # 2
                q.append(nxt)
    
    # now가 g와 같아지는 순간이 없다면
    return "use the stairs"

print(bfs(s))
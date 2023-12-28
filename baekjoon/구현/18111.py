'''
[마인크래프트]
- 없애는데 2초
- 추가하는데 1초
작업에 걸리는 최소 시간, 땅의 높이가 가장 높은 것

* 높이를 기준으로 생각해보자.
- 최종 높이는 가장 낮은 높이 ~ 가장 높은 높이 사이
- 이 구간을 모두 탐색하면서 가능한대로 최소 구하기
- 블럭을 넣는게 시간이 가장 작으므로 넣지 못하면 바로 break

By chatGPT
: 높은 땅을 낮출 때 인벤토리에 블록이 "추가"되는 것을 고려하지 않았습니다.
'''
n, m, block = map(int, input().split())

graph = []
mini, maxi = 1e9, 0
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        mini = min(mini, row[j])
        maxi = max(maxi, row[j])
    graph.append(row)

def check(h):
    take = 0  # 주운 블럭 수
    use = 0   # 쓰는 블럭 수
    for i in range(n):
        for j in range(m):
            if h > graph[i][j]:
                use += (h-graph[i][j])
            else:  # h <= graph[i][j] : elif보다 빠름
                take += (graph[i][j]-h)
    
    if use > take + block:
        return None

    time = 2*take + use
    return time

answer = 1e9  # 최소 시간 구하기
height = 0  # 최종 높이
for h in range(maxi, mini-1, -1):
    tmp = check(h)  # 시도 시간
    if tmp != None and tmp < answer:
        answer = tmp
        height = h

print(answer, height)
                